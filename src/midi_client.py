import logging
import time
from enum import Flag

from pyalsa import alsaseq
from app_infos import APP_NAME

from voxou import Voxou
from midi_enums import MidiConnectState


_logger = logging.getLogger(__name__)

VALVETRONIX_CLIENT_NAME = 'Valvetronix X'
VALVETRONIX_PORT_NAME = 'Valvetronix X MIDI 1'
AUTO_CONNECT = True


class Connected(Flag):
    NONE = 0x0
    INPUT = 0x1
    OUTPUT = 0x2
    BOTH = INPUT | OUTPUT
 
 
class MidiClient:
    def __init__(self):
        self._midi_connect_state = MidiConnectState.ABSENT_DEVICE
        self._vtronix_client_id = 0
        self._vtronix_port_id = 0

        self.seq = alsaseq.Sequencer(clientname=APP_NAME)

        port_type = (alsaseq.SEQ_PORT_TYPE_MIDI_GENERIC
                     | alsaseq.SEQ_PORT_TYPE_APPLICATION)
        port_caps = (alsaseq.SEQ_PORT_CAP_WRITE
                     | alsaseq.SEQ_PORT_CAP_SUBS_WRITE
                     | alsaseq.SEQ_PORT_CAP_READ
                     | alsaseq.SEQ_PORT_CAP_SUBS_READ)
        self._port_id = self.seq.create_simple_port(
            "Valvetronix", port_type, port_caps)

        self.seq.connect_ports(
            (alsaseq.SEQ_CLIENT_SYSTEM, alsaseq.SEQ_PORT_SYSTEM_ANNOUNCE),
            (self.seq.client_id, self._port_id))

        self.stopping = False
        self.voxou: Voxou = None
        self._midi_drain_pending = False
        self._pending_send = False

    def restart(self, new_name: str):
        if self._midi_connect_state is not MidiConnectState.ABSENT_DEVICE:
            self.set_midi_connect_state(MidiConnectState.DISCONNECTED)

        del self.seq
        self.seq = alsaseq.Sequencer(clientname=new_name)

        port_type = (alsaseq.SEQ_PORT_TYPE_MIDI_GENERIC
                     | alsaseq.SEQ_PORT_TYPE_APPLICATION)
        port_caps = (alsaseq.SEQ_PORT_CAP_WRITE
                     | alsaseq.SEQ_PORT_CAP_SUBS_WRITE
                     | alsaseq.SEQ_PORT_CAP_READ
                     | alsaseq.SEQ_PORT_CAP_SUBS_READ)
        self._port_id = self.seq.create_simple_port(
            "Valvetronix", port_type, port_caps)

        self.seq.connect_ports(
            (alsaseq.SEQ_CLIENT_SYSTEM, alsaseq.SEQ_PORT_SYSTEM_ANNOUNCE),
            (self.seq.client_id, self._port_id))

        self._midi_drain_pending = False
        self._pending_send = False
        self.startup_vox_check()

    def set_voxou(self, voxou: Voxou):
        self.voxou = voxou
        self.voxou.set_midi_out_func(self.send_to_vox)
        self.startup_vox_check()

    def set_midi_connect_state(self, connect_state: MidiConnectState):
        self._midi_connect_state = connect_state
        self.voxou.set_midi_connect_state(connect_state)

    def startup_vox_check(self):
        clients = self.seq.connection_list()

        for client in clients:
            client_name, client_id, port_list = client
            if client_name != VALVETRONIX_CLIENT_NAME:
                continue
            
            for port_name, port_id, connection_list in port_list:
                if port_name != VALVETRONIX_PORT_NAME:
                    continue
                
                port_info = self.seq.get_port_info(port_id, client_id)
                if port_info['type'] & alsaseq.SEQ_PORT_TYPE_APPLICATION:
                    # port is not physical, it is not the Valvetronix
                    _logger.warning(
                        "Did not accept to recognize Valvetronix "
                        "because it is not an hardware port")
                    continue
                
                _logger.info('Valvetronix is present !')
                
                self._vtronix_client_id = client_id
                self._vtronix_port_id = port_id
                self.set_midi_connect_state(MidiConnectState.DISCONNECTED)
                if AUTO_CONNECT:
                    self.connect_to_vox()
                return

    def connect_to_vox(self):
        if self._midi_connect_state is MidiConnectState.ABSENT_DEVICE:
            _logger.warning("Will not try to connect to device, "
                            "device is absent.")
            return
        
        if self._midi_connect_state in (MidiConnectState.CONNECTED,
                                       MidiConnectState.CONNECTED):
            _logger.warning("Will not try to connect to device, "
                            "already connected to device.")
            return
        
        if self._midi_connect_state is not MidiConnectState.OUTPUT_ONLY:
            try:
                self.seq.connect_ports(
                    (self.seq.client_id, self._port_id),
                    (self._vtronix_client_id, self._vtronix_port_id),
                    0, 0, 0, 0)
            except BaseException as e:
                _logger.error(
                    'Failed to connect to Valvetronix Output !\n'
                    f'{str(e)}')

        if self._midi_connect_state is not MidiConnectState.INPUT_ONLY:   
            try:
                self.seq.connect_ports(
                    (self._vtronix_client_id, self._vtronix_port_id),
                    (self.seq.client_id, self._port_id),
                    0, 0, 0, 0)
            except BaseException as e:
                _logger.error(
                    'Failed to connect to Valvetronix input !\n'
                    f'{str(e)}')

    def read_events(self):
        midi_events = self.seq.receive_events()
        for event in midi_events:
            data = event.get_data()
            
            if event.type is alsaseq.SEQ_EVENT_SYSEX:
                int_list: list[int] = data['ext']
                if self.voxou is not None:
                    self.voxou.receive_sysex(int_list)

            elif event.type is alsaseq.SEQ_EVENT_PORT_START:
                client_id, port_id = data['addr.client'], data['addr.port']
                try:
                    client_info = self.seq.get_client_info(client_id)
                    port_info = self.seq.get_port_info(port_id, client_id)
                except:
                    continue
                
                n_tries = 0
                client_outed = False
                
                while client_info['name'] == f'Client-{client_id}':
                    time.sleep(0.010)
                    try:
                        client_info = self.seq.get_client_info(client_id)
                    except:
                        client_outed = True
                        break
                
                    n_tries += 1
                    if n_tries >= 5:
                        break
                
                if (client_outed
                        or client_info['name'] != VALVETRONIX_CLIENT_NAME
                        or port_info['name'] != VALVETRONIX_PORT_NAME):
                    continue
                
                self._vtronix_client_id = client_id
                self._vtronix_port_id = port_id
                self.set_midi_connect_state(MidiConnectState.DISCONNECTED)

                if AUTO_CONNECT:
                    self.connect_to_vox()                   
            
            elif event.type is alsaseq.SEQ_EVENT_PORT_EXIT:
                client_id, port_id = data['addr.client'], data['addr.port']
                if ((client_id, port_id)
                        == (self._vtronix_client_id, self._vtronix_port_id)):
                    self.set_midi_connect_state(MidiConnectState.ABSENT_DEVICE)
                    
            elif event.type is alsaseq.SEQ_EVENT_PORT_SUBSCRIBED:
                if self._midi_connect_state is MidiConnectState.ABSENT_DEVICE:
                    continue
                
                ex_midi_conn_state = self._midi_connect_state
                  
                if (data['connect.sender.client'] == self._vtronix_client_id
                        and data['connect.sender.port'] == self._vtronix_port_id
                        and data['connect.dest.client'] == self.seq.client_id
                        and data['connect.dest.port'] == self._port_id):

                    if self._midi_connect_state is MidiConnectState.OUTPUT_ONLY:
                        self.set_midi_connect_state(MidiConnectState.CONNECTED)
                    elif self._midi_connect_state is MidiConnectState.DISCONNECTED:
                        self.set_midi_connect_state(MidiConnectState.INPUT_ONLY)

                elif (data['connect.sender.client'] == self.seq.client_id
                        and data['connect.sender.port'] == self._port_id
                        and data['connect.dest.client'] == self._vtronix_client_id
                        and data['connect.dest.port'] == self._vtronix_port_id):

                    if self._midi_connect_state is MidiConnectState.INPUT_ONLY:
                        self.set_midi_connect_state(MidiConnectState.CONNECTED)
                    elif self._midi_connect_state is MidiConnectState.DISCONNECTED:
                        self.set_midi_connect_state(MidiConnectState.OUTPUT_ONLY)
                    
                if (ex_midi_conn_state is not self._midi_connect_state
                        and self._midi_connect_state
                        is MidiConnectState.CONNECTED):
                    # ask to voxou to send the announce messages
                    self.voxou.start_communication()
            
            elif event.type is alsaseq.SEQ_EVENT_PORT_UNSUBSCRIBED:
                if self._midi_connect_state is MidiConnectState.ABSENT_DEVICE:
                    continue
                
                if (data['connect.sender.client'] == self._vtronix_client_id
                        and data['connect.sender.port'] == self._vtronix_port_id
                        and data['connect.dest.client'] == self.seq.client_id
                        and data['connect.dest.port'] == self._port_id):
                    if self._midi_connect_state is MidiConnectState.INPUT_ONLY:
                        self.set_midi_connect_state(MidiConnectState.DISCONNECTED)
                    elif self._midi_connect_state is MidiConnectState.CONNECTED:
                        self.set_midi_connect_state(MidiConnectState.OUTPUT_ONLY)

                elif (data['connect.sender.client'] == self.seq.client_id
                        and data['connect.sender.port'] == self._port_id
                        and data['connect.dest.client'] == self._vtronix_client_id
                        and data['connect.dest.port'] == self._vtronix_port_id):
                    if self._midi_connect_state is MidiConnectState.OUTPUT_ONLY:
                        self.set_midi_connect_state(MidiConnectState.DISCONNECTED)
                    elif self._midi_connect_state is MidiConnectState.CONNECTED:
                        self.set_midi_connect_state(MidiConnectState.INPUT_ONLY)

    def send_to_vox(self, args: list[int]):
        event = alsaseq.SeqEvent(alsaseq.SEQ_EVENT_SYSEX)
        event.set_data({'ext': args})
        event.source = (self.seq.client_id, self._port_id)
        self.seq.output_event(event)

        try:
            self.seq.drain_output()
        except:
            self._midi_drain_pending = True
            _logger.warning('midi pool unnavailable, trying again')

        self._pending_send = True

    def flush(self):
        if not self._pending_send:
            return

        if self._midi_drain_pending:
            try:
                self.seq.drain_output()
                self.seq._midi_drain_pending = False
            except:
                _logger.warning('midi pool unnavailable, trying again')

        self.seq.sync_output_queue()
        self._pending_send = False


midi_client = MidiClient()


def init(voxou: Voxou):
    midi_client.set_voxou(voxou)

def restart(new_name: str):
    midi_client.restart(new_name)

def stop():
    midi_client.stopping = True

def run_loop():
    if midi_client.voxou is None:
        _logger.error('voxou must be set before to run midi main loop')
        return

    while not midi_client.stopping:
        midi_client.read_events()
        midi_client.flush()
        time.sleep(0.001)