# Form implementation generated from reading ui file 'resources/ui/full_amp_import.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DialogFullAmpImport(object):
    def setupUi(self, DialogFullAmpImport):
        DialogFullAmpImport.setObjectName("DialogFullAmpImport")
        DialogFullAmpImport.resize(348, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogFullAmpImport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxFile = QtWidgets.QGroupBox(parent=DialogFullAmpImport)
        self.groupBoxFile.setTitle("")
        self.groupBoxFile.setObjectName("groupBoxFile")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxFile)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBoxFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboBoxAmpConfig = QtWidgets.QComboBox(parent=self.groupBoxFile)
        self.comboBoxAmpConfig.setObjectName("comboBoxAmpConfig")
        self.horizontalLayout_3.addWidget(self.comboBoxAmpConfig)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.framePathSelector = QtWidgets.QFrame(parent=self.groupBoxFile)
        self.framePathSelector.setEnabled(False)
        self.framePathSelector.setObjectName("framePathSelector")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.framePathSelector)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.framePathSelector)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditPath = QtWidgets.QLineEdit(parent=self.framePathSelector)
        self.lineEditPath.setReadOnly(True)
        self.lineEditPath.setObjectName("lineEditPath")
        self.horizontalLayout.addWidget(self.lineEditPath)
        self.toolButtonBrowse = QtWidgets.QToolButton(parent=self.framePathSelector)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.toolButtonBrowse.setIcon(icon)
        self.toolButtonBrowse.setObjectName("toolButtonBrowse")
        self.horizontalLayout.addWidget(self.toolButtonBrowse)
        self.verticalLayout_3.addWidget(self.framePathSelector)
        self.labelInvalidFile = QtWidgets.QLabel(parent=self.groupBoxFile)
        self.labelInvalidFile.setStyleSheet("QLabel{color:red}")
        self.labelInvalidFile.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelInvalidFile.setObjectName("labelInvalidFile")
        self.verticalLayout_3.addWidget(self.labelInvalidFile)
        self.verticalLayout.addWidget(self.groupBoxFile)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBoxMainAction = QtWidgets.QGroupBox(parent=DialogFullAmpImport)
        self.groupBoxMainAction.setEnabled(False)
        self.groupBoxMainAction.setTitle("")
        self.groupBoxMainAction.setObjectName("groupBoxMainAction")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxMainAction)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBoxMainAction)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.comboBoxMainChoice = QtWidgets.QComboBox(parent=self.groupBoxMainAction)
        self.comboBoxMainChoice.setObjectName("comboBoxMainChoice")
        self.verticalLayout_2.addWidget(self.comboBoxMainChoice)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.groupBoxMainAction)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageFullAmp = QtWidgets.QWidget()
        self.pageFullAmp.setObjectName("pageFullAmp")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pageFullAmp)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBoxUserBanks = QtWidgets.QCheckBox(parent=self.pageFullAmp)
        self.checkBoxUserBanks.setChecked(True)
        self.checkBoxUserBanks.setObjectName("checkBoxUserBanks")
        self.verticalLayout_4.addWidget(self.checkBoxUserBanks)
        self.checkBoxAmpFx = QtWidgets.QCheckBox(parent=self.pageFullAmp)
        self.checkBoxAmpFx.setChecked(False)
        self.checkBoxAmpFx.setObjectName("checkBoxAmpFx")
        self.verticalLayout_4.addWidget(self.checkBoxAmpFx)
        self.checkBoxCurrentProgram = QtWidgets.QCheckBox(parent=self.pageFullAmp)
        self.checkBoxCurrentProgram.setChecked(False)
        self.checkBoxCurrentProgram.setObjectName("checkBoxCurrentProgram")
        self.verticalLayout_4.addWidget(self.checkBoxCurrentProgram)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.pageFullAmp)
        self.pageAmpFx = QtWidgets.QWidget()
        self.pageAmpFx.setObjectName("pageAmpFx")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.pageAmpFx)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.groupBox = QtWidgets.QGroupBox(parent=self.pageAmpFx)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBoxAmpFxFrom = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBoxAmpFxFrom.setObjectName("comboBoxAmpFxFrom")
        self.horizontalLayout_2.addWidget(self.comboBoxAmpFxFrom)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.labelAmpFxAmp = QtWidgets.QLabel(parent=self.groupBox)
        self.labelAmpFxAmp.setObjectName("labelAmpFxAmp")
        self.verticalLayout_5.addWidget(self.labelAmpFxAmp)
        self.labelAmpFxPedal1 = QtWidgets.QLabel(parent=self.groupBox)
        self.labelAmpFxPedal1.setObjectName("labelAmpFxPedal1")
        self.verticalLayout_5.addWidget(self.labelAmpFxPedal1)
        self.labelAmpFxPedal2 = QtWidgets.QLabel(parent=self.groupBox)
        self.labelAmpFxPedal2.setObjectName("labelAmpFxPedal2")
        self.verticalLayout_5.addWidget(self.labelAmpFxPedal2)
        self.labelAmpFxReverb = QtWidgets.QLabel(parent=self.groupBox)
        self.labelAmpFxReverb.setObjectName("labelAmpFxReverb")
        self.verticalLayout_5.addWidget(self.labelAmpFxReverb)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.label_3 = QtWidgets.QLabel(parent=self.pageAmpFx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.comboBoxAmpFxTo = QtWidgets.QComboBox(parent=self.pageAmpFx)
        self.comboBoxAmpFxTo.setObjectName("comboBoxAmpFxTo")
        self.horizontalLayout_5.addWidget(self.comboBoxAmpFxTo)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.pageAmpFx)
        self.pageSingleProgram = QtWidgets.QWidget()
        self.pageSingleProgram.setObjectName("pageSingleProgram")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.pageSingleProgram)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.pageSingleProgram)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.comboBoxSingleFrom = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBoxSingleFrom.setObjectName("comboBoxSingleFrom")
        self.horizontalLayout_6.addWidget(self.comboBoxSingleFrom)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.lineEditSingleProgramName = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditSingleProgramName.setReadOnly(True)
        self.lineEditSingleProgramName.setObjectName("lineEditSingleProgramName")
        self.verticalLayout_6.addWidget(self.lineEditSingleProgramName)
        self.labelSingleAmp = QtWidgets.QLabel(parent=self.groupBox_2)
        self.labelSingleAmp.setObjectName("labelSingleAmp")
        self.verticalLayout_6.addWidget(self.labelSingleAmp)
        self.labelSinglePedal1 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.labelSinglePedal1.setObjectName("labelSinglePedal1")
        self.verticalLayout_6.addWidget(self.labelSinglePedal1)
        self.labelSinglePedal2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.labelSinglePedal2.setObjectName("labelSinglePedal2")
        self.verticalLayout_6.addWidget(self.labelSinglePedal2)
        self.labelSingleReverb = QtWidgets.QLabel(parent=self.groupBox_2)
        self.labelSingleReverb.setObjectName("labelSingleReverb")
        self.verticalLayout_6.addWidget(self.labelSingleReverb)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.label_5 = QtWidgets.QLabel(parent=self.pageSingleProgram)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.comboBoxSingleTo = QtWidgets.QComboBox(parent=self.pageSingleProgram)
        self.comboBoxSingleTo.setObjectName("comboBoxSingleTo")
        self.horizontalLayout_7.addWidget(self.comboBoxSingleTo)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.pageSingleProgram)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addWidget(self.groupBoxMainAction)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=DialogFullAmpImport)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Apply|QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogFullAmpImport)
        self.buttonBox.accepted.connect(DialogFullAmpImport.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogFullAmpImport.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogFullAmpImport)

    def retranslateUi(self, DialogFullAmpImport):
        _translate = QtCore.QCoreApplication.translate
        DialogFullAmpImport.setWindowTitle(_translate("DialogFullAmpImport", "Full Amp config import"))
        self.label_6.setText(_translate("DialogFullAmpImport", "Saved Amp Config"))
        self.label.setText(_translate("DialogFullAmpImport", "File"))
        self.toolButtonBrowse.setText(_translate("DialogFullAmpImport", "..."))
        self.labelInvalidFile.setText(_translate("DialogFullAmpImport", "This file is not a valid amp config file !"))
        self.label_7.setText(_translate("DialogFullAmpImport", "What do you want to import from this saved config ?"))
        self.checkBoxUserBanks.setText(_translate("DialogFullAmpImport", "User Banks"))
        self.checkBoxAmpFx.setText(_translate("DialogFullAmpImport", "User AmpFxs"))
        self.checkBoxCurrentProgram.setText(_translate("DialogFullAmpImport", "Current Program"))
        self.label_2.setText(_translate("DialogFullAmpImport", "From"))
        self.labelAmpFxAmp.setText(_translate("DialogFullAmpImport", "Amp"))
        self.labelAmpFxPedal1.setText(_translate("DialogFullAmpImport", "Pedal1"))
        self.labelAmpFxPedal2.setText(_translate("DialogFullAmpImport", "Pedal2"))
        self.labelAmpFxReverb.setText(_translate("DialogFullAmpImport", "Reverb"))
        self.label_3.setText(_translate("DialogFullAmpImport", "To"))
        self.label_4.setText(_translate("DialogFullAmpImport", "From"))
        self.labelSingleAmp.setText(_translate("DialogFullAmpImport", "Amp"))
        self.labelSinglePedal1.setText(_translate("DialogFullAmpImport", "Pedal1"))
        self.labelSinglePedal2.setText(_translate("DialogFullAmpImport", "Pedal2"))
        self.labelSingleReverb.setText(_translate("DialogFullAmpImport", "Reverb"))
        self.label_5.setText(_translate("DialogFullAmpImport", "To"))
