# Form implementation generated from reading ui file 'resources/ui/about_oscitronix.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DialogAboutOscitronix(object):
    def setupUi(self, DialogAboutOscitronix):
        DialogAboutOscitronix.setObjectName("DialogAboutOscitronix")
        DialogAboutOscitronix.resize(452, 284)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogAboutOscitronix)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=DialogAboutOscitronix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/main_icon/128x128/oscitronix.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelOsciAndVersion = QtWidgets.QLabel(parent=DialogAboutOscitronix)
        self.labelOsciAndVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelOsciAndVersion.setObjectName("labelOsciAndVersion")
        self.verticalLayout_3.addWidget(self.labelOsciAndVersion)
        self.labelAllText = QtWidgets.QLabel(parent=DialogAboutOscitronix)
        self.labelAllText.setWordWrap(True)
        self.labelAllText.setOpenExternalLinks(True)
        self.labelAllText.setObjectName("labelAllText")
        self.verticalLayout_3.addWidget(self.labelAllText)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=DialogAboutOscitronix)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogAboutOscitronix)
        self.buttonBox.accepted.connect(DialogAboutOscitronix.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogAboutOscitronix.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAboutOscitronix)

    def retranslateUi(self, DialogAboutOscitronix):
        _translate = QtCore.QCoreApplication.translate
        DialogAboutOscitronix.setWindowTitle(_translate("DialogAboutOscitronix", "About OsciTronix"))
        self.labelOsciAndVersion.setText(_translate("DialogAboutOscitronix", "<html><head/><body><p><span style=\" font-weight:600;\">Oscitronix</span></p><p>version : %s</p></body></html>"))
        self.labelAllText.setText(_translate("DialogAboutOscitronix", "<html><head/><body><p>OsciTronix is a controller for VT20X, VT40X and VT100X VOX guitar amps*.</p><p>It is written in python with the Qt framework.</p><p><span style=\" font-style:italic;\">* Registered trademark </span><br/></p><p align=\"right\">Copyright (C) 2024 houston4444</p><p><br/></p></body></html>"))
