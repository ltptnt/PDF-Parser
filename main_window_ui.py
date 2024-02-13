# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_window.ui'
#
# Created by: Qt User Interface Compiler version 6.6.1
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QAbstractSpinBox,
    QComboBox,
    QDateEdit,
    QFrame,
    QGridLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QTextEdit,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(700, 1240)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 1240))
        MainWindow.setMaximumSize(QSize(700, 1269))
        font = QFont()
        font.setFamilies(["Open Sans"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(10000, 10000))
        font1 = QFont()
        font1.setFamilies(["Open Sans"])
        font1.setPointSize(13)
        self.centralwidget.setFont(font1)
        self.centralwidget.setFocusPolicy(Qt.ClickFocus)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainApp = QGridLayout()
        self.mainApp.setSpacing(6)
        self.mainApp.setObjectName("mainApp")
        self.mainApp.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mainApp.setHorizontalSpacing(20)
        self.mainApp.setVerticalSpacing(10)
        self.mainApp.setContentsMargins(10, 10, 10, 10)
        self.line9 = QFrame(self.centralwidget)
        self.line9.setObjectName("line9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line9.sizePolicy().hasHeightForWidth())
        self.line9.setSizePolicy(sizePolicy1)
        self.line9.setMinimumSize(QSize(1, 1))
        self.line9.setFont(font1)
        self.line9.setLayoutDirection(Qt.LeftToRight)
        self.line9.setFrameShadow(QFrame.Plain)
        self.line9.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line9, 17, 0, 1, 2)

        self.bloodPressureLabel = QLabel(self.centralwidget)
        self.bloodPressureLabel.setObjectName("bloodPressureLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.bloodPressureLabel.sizePolicy().hasHeightForWidth()
        )
        self.bloodPressureLabel.setSizePolicy(sizePolicy2)
        self.bloodPressureLabel.setMinimumSize(QSize(230, 0))
        self.bloodPressureLabel.setFont(font1)

        self.mainApp.addWidget(self.bloodPressureLabel, 14, 0, 1, 1)

        self.bloodPressureLineEdit = QLineEdit(self.centralwidget)
        self.bloodPressureLineEdit.setObjectName("bloodPressureLineEdit")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.bloodPressureLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.bloodPressureLineEdit.setSizePolicy(sizePolicy3)
        self.bloodPressureLineEdit.setMinimumSize(QSize(410, 0))
        self.bloodPressureLineEdit.setFont(font1)

        self.mainApp.addWidget(self.bloodPressureLineEdit, 14, 1, 1, 1)

        self.line10 = QFrame(self.centralwidget)
        self.line10.setObjectName("line10")
        sizePolicy1.setHeightForWidth(self.line10.sizePolicy().hasHeightForWidth())
        self.line10.setSizePolicy(sizePolicy1)
        self.line10.setMinimumSize(QSize(1, 1))
        self.line10.setFont(font1)
        self.line10.setLayoutDirection(Qt.LeftToRight)
        self.line10.setFrameShadow(QFrame.Plain)
        self.line10.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line10, 19, 0, 1, 2)

        self.line11_2 = QFrame(self.centralwidget)
        self.line11_2.setObjectName("line11_2")
        sizePolicy1.setHeightForWidth(self.line11_2.sizePolicy().hasHeightForWidth())
        self.line11_2.setSizePolicy(sizePolicy1)
        self.line11_2.setMinimumSize(QSize(1, 1))
        self.line11_2.setFont(font1)
        self.line11_2.setLayoutDirection(Qt.LeftToRight)
        self.line11_2.setFrameShadow(QFrame.Plain)
        self.line11_2.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line11_2, 23, 0, 1, 2)

        self.titleGridLayout = QGridLayout()
        self.titleGridLayout.setSpacing(6)
        self.titleGridLayout.setObjectName("titleGridLayout")
        self.titleGridLayout.setContentsMargins(-1, -1, -1, 0)
        self.getInformationButton = QPushButton(self.centralwidget)
        self.getInformationButton.setObjectName("getInformationButton")
        sizePolicy.setHeightForWidth(
            self.getInformationButton.sizePolicy().hasHeightForWidth()
        )
        self.getInformationButton.setSizePolicy(sizePolicy)
        self.getInformationButton.setMinimumSize(QSize(170, 28))
        self.getInformationButton.setFont(font1)

        self.titleGridLayout.addWidget(self.getInformationButton, 1, 1, 1, 1)

        self.createDocumentButton = QPushButton(self.centralwidget)
        self.createDocumentButton.setObjectName("createDocumentButton")
        sizePolicy.setHeightForWidth(
            self.createDocumentButton.sizePolicy().hasHeightForWidth()
        )
        self.createDocumentButton.setSizePolicy(sizePolicy)
        self.createDocumentButton.setMinimumSize(QSize(170, 28))
        self.createDocumentButton.setFont(font1)

        self.titleGridLayout.addWidget(self.createDocumentButton, 2, 1, 1, 1)

        self.templateSelectorComboBox = QComboBox(self.centralwidget)
        self.templateSelectorComboBox.setObjectName("templateSelectorComboBox")
        sizePolicy.setHeightForWidth(
            self.templateSelectorComboBox.sizePolicy().hasHeightForWidth()
        )
        self.templateSelectorComboBox.setSizePolicy(sizePolicy)
        self.templateSelectorComboBox.setMinimumSize(QSize(170, 28))
        self.templateSelectorComboBox.setFont(font1)
        self.templateSelectorComboBox.setFrame(True)

        self.titleGridLayout.addWidget(self.templateSelectorComboBox, 0, 1, 1, 1)

        self.TitleText = QLabel(self.centralwidget)
        self.TitleText.setObjectName("TitleText")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.TitleText.sizePolicy().hasHeightForWidth())
        self.TitleText.setSizePolicy(sizePolicy4)
        self.TitleText.setMinimumSize(QSize(0, 120))
        font2 = QFont()
        font2.setFamilies(["Open Sans"])
        font2.setPointSize(20)
        self.TitleText.setFont(font2)
        self.TitleText.setIndent(10)

        self.titleGridLayout.addWidget(self.TitleText, 0, 0, 3, 1)

        self.mainApp.addLayout(self.titleGridLayout, 0, 0, 1, 2)

        self.doctorPreferredContactLineEdit = QLineEdit(self.centralwidget)
        self.doctorPreferredContactLineEdit.setObjectName(
            "doctorPreferredContactLineEdit"
        )
        sizePolicy3.setHeightForWidth(
            self.doctorPreferredContactLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.doctorPreferredContactLineEdit.setSizePolicy(sizePolicy3)
        self.doctorPreferredContactLineEdit.setMinimumSize(QSize(410, 0))
        self.doctorPreferredContactLineEdit.setFont(font1)

        self.mainApp.addWidget(self.doctorPreferredContactLineEdit, 28, 1, 1, 1)

        self.crClLineEdit = QLineEdit(self.centralwidget)
        self.crClLineEdit.setObjectName("crClLineEdit")
        sizePolicy3.setHeightForWidth(
            self.crClLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.crClLineEdit.setSizePolicy(sizePolicy3)
        self.crClLineEdit.setMinimumSize(QSize(410, 0))
        self.crClLineEdit.setFont(font1)

        self.mainApp.addWidget(self.crClLineEdit, 18, 1, 1, 1)

        self.addressLabel = QLabel(self.centralwidget)
        self.addressLabel.setObjectName("addressLabel")
        sizePolicy2.setHeightForWidth(
            self.addressLabel.sizePolicy().hasHeightForWidth()
        )
        self.addressLabel.setSizePolicy(sizePolicy2)
        self.addressLabel.setMinimumSize(QSize(230, 0))
        self.addressLabel.setFont(font1)

        self.mainApp.addWidget(self.addressLabel, 6, 0, 1, 1)

        self.medicationsLabel = QLabel(self.centralwidget)
        self.medicationsLabel.setObjectName("medicationsLabel")
        sizePolicy2.setHeightForWidth(
            self.medicationsLabel.sizePolicy().hasHeightForWidth()
        )
        self.medicationsLabel.setSizePolicy(sizePolicy2)
        self.medicationsLabel.setMinimumSize(QSize(230, 0))
        self.medicationsLabel.setFont(font1)

        self.mainApp.addWidget(self.medicationsLabel, 22, 0, 1, 1)

        self.line16 = QFrame(self.centralwidget)
        self.line16.setObjectName("line16")
        sizePolicy1.setHeightForWidth(self.line16.sizePolicy().hasHeightForWidth())
        self.line16.setSizePolicy(sizePolicy1)
        self.line16.setMinimumSize(QSize(1, 1))
        self.line16.setFont(font1)
        self.line16.setLayoutDirection(Qt.LeftToRight)
        self.line16.setFrameShadow(QFrame.Plain)
        self.line16.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line16, 33, 0, 1, 2)

        self.line14 = QFrame(self.centralwidget)
        self.line14.setObjectName("line14")
        sizePolicy1.setHeightForWidth(self.line14.sizePolicy().hasHeightForWidth())
        self.line14.setSizePolicy(sizePolicy1)
        self.line14.setMinimumSize(QSize(1, 1))
        self.line14.setFont(font1)
        self.line14.setLayoutDirection(Qt.LeftToRight)
        self.line14.setFrameShadow(QFrame.Plain)
        self.line14.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line14, 29, 0, 1, 2)

        self.creatineLineEdit = QLineEdit(self.centralwidget)
        self.creatineLineEdit.setObjectName("creatineLineEdit")
        sizePolicy3.setHeightForWidth(
            self.creatineLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.creatineLineEdit.setSizePolicy(sizePolicy3)
        self.creatineLineEdit.setMinimumSize(QSize(410, 0))
        self.creatineLineEdit.setFont(font1)

        self.mainApp.addWidget(self.creatineLineEdit, 16, 1, 1, 1)

        self.line12 = QFrame(self.centralwidget)
        self.line12.setObjectName("line12")
        sizePolicy1.setHeightForWidth(self.line12.sizePolicy().hasHeightForWidth())
        self.line12.setSizePolicy(sizePolicy1)
        self.line12.setMinimumSize(QSize(1, 1))
        self.line12.setFont(font1)
        self.line12.setLayoutDirection(Qt.LeftToRight)
        self.line12.setFrameShadow(QFrame.Plain)
        self.line12.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line12, 25, 0, 1, 2)

        self.reasonForReferralLineEdit = QLineEdit(self.centralwidget)
        self.reasonForReferralLineEdit.setObjectName("reasonForReferralLineEdit")
        sizePolicy3.setHeightForWidth(
            self.reasonForReferralLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.reasonForReferralLineEdit.setSizePolicy(sizePolicy3)
        self.reasonForReferralLineEdit.setMinimumSize(QSize(410, 0))
        self.reasonForReferralLineEdit.setFont(font1)

        self.mainApp.addWidget(self.reasonForReferralLineEdit, 30, 1, 1, 1)

        self.doctorProviderNumberLabel = QLabel(self.centralwidget)
        self.doctorProviderNumberLabel.setObjectName("doctorProviderNumberLabel")
        sizePolicy2.setHeightForWidth(
            self.doctorProviderNumberLabel.sizePolicy().hasHeightForWidth()
        )
        self.doctorProviderNumberLabel.setSizePolicy(sizePolicy2)
        self.doctorProviderNumberLabel.setMinimumSize(QSize(230, 0))
        self.doctorProviderNumberLabel.setFont(font1)

        self.mainApp.addWidget(self.doctorProviderNumberLabel, 26, 0, 1, 1)

        self.medicareNumberLabel = QLabel(self.centralwidget)
        self.medicareNumberLabel.setObjectName("medicareNumberLabel")
        sizePolicy2.setHeightForWidth(
            self.medicareNumberLabel.sizePolicy().hasHeightForWidth()
        )
        self.medicareNumberLabel.setSizePolicy(sizePolicy2)
        self.medicareNumberLabel.setMinimumSize(QSize(230, 0))
        self.medicareNumberLabel.setFont(font1)

        self.mainApp.addWidget(self.medicareNumberLabel, 8, 0, 1, 1)

        self.medicationsTextEdit = QTextEdit(self.centralwidget)
        self.medicationsTextEdit.setObjectName("medicationsTextEdit")
        sizePolicy3.setHeightForWidth(
            self.medicationsTextEdit.sizePolicy().hasHeightForWidth()
        )
        self.medicationsTextEdit.setSizePolicy(sizePolicy3)
        self.medicationsTextEdit.setMinimumSize(QSize(410, 90))
        self.medicationsTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.medicationsTextEdit.setFont(font1)
        self.medicationsTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.medicationsTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.medicationsTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.medicationsTextEdit.setTabChangesFocus(True)
        self.medicationsTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.mainApp.addWidget(self.medicationsTextEdit, 22, 1, 1, 1)

        self.dOBDateEdit = QDateEdit(self.centralwidget)
        self.dOBDateEdit.setObjectName("dOBDateEdit")
        sizePolicy3.setHeightForWidth(self.dOBDateEdit.sizePolicy().hasHeightForWidth())
        self.dOBDateEdit.setSizePolicy(sizePolicy3)
        self.dOBDateEdit.setMinimumSize(QSize(410, 0))
        self.dOBDateEdit.setFont(font1)
        self.dOBDateEdit.setWrapping(False)
        self.dOBDateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dOBDateEdit.setProperty("showGroupSeparator", False)
        self.dOBDateEdit.setCalendarPopup(True)

        self.mainApp.addWidget(self.dOBDateEdit, 4, 1, 1, 1)

        self.crClLabel = QLabel(self.centralwidget)
        self.crClLabel.setObjectName("crClLabel")
        sizePolicy2.setHeightForWidth(self.crClLabel.sizePolicy().hasHeightForWidth())
        self.crClLabel.setSizePolicy(sizePolicy2)
        self.crClLabel.setMinimumSize(QSize(230, 0))
        self.crClLabel.setFont(font1)

        self.mainApp.addWidget(self.crClLabel, 18, 0, 1, 1)

        self.line3 = QFrame(self.centralwidget)
        self.line3.setObjectName("line3")
        sizePolicy1.setHeightForWidth(self.line3.sizePolicy().hasHeightForWidth())
        self.line3.setSizePolicy(sizePolicy1)
        self.line3.setMinimumSize(QSize(1, 1))
        self.line3.setFont(font1)
        self.line3.setLayoutDirection(Qt.LeftToRight)
        self.line3.setFrameShadow(QFrame.Plain)
        self.line3.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line3, 5, 0, 1, 2)

        self.addressLineEdit = QLineEdit(self.centralwidget)
        self.addressLineEdit.setObjectName("addressLineEdit")
        sizePolicy3.setHeightForWidth(
            self.addressLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.addressLineEdit.setSizePolicy(sizePolicy3)
        self.addressLineEdit.setMinimumSize(QSize(410, 0))
        self.addressLineEdit.setFont(font1)

        self.mainApp.addWidget(self.addressLineEdit, 6, 1, 1, 1)

        self.line6 = QFrame(self.centralwidget)
        self.line6.setObjectName("line6")
        sizePolicy1.setHeightForWidth(self.line6.sizePolicy().hasHeightForWidth())
        self.line6.setSizePolicy(sizePolicy1)
        self.line6.setMinimumSize(QSize(1, 1))
        self.line6.setFont(font1)
        self.line6.setLayoutDirection(Qt.LeftToRight)
        self.line6.setFrameShadow(QFrame.Plain)
        self.line6.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line6, 11, 0, 1, 2)

        self.dOBLabel = QLabel(self.centralwidget)
        self.dOBLabel.setObjectName("dOBLabel")
        sizePolicy2.setHeightForWidth(self.dOBLabel.sizePolicy().hasHeightForWidth())
        self.dOBLabel.setSizePolicy(sizePolicy2)
        self.dOBLabel.setMinimumSize(QSize(230, 0))
        self.dOBLabel.setFont(font1)

        self.mainApp.addWidget(self.dOBLabel, 4, 0, 1, 1)

        self.line2 = QFrame(self.centralwidget)
        self.line2.setObjectName("line2")
        sizePolicy1.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy1)
        self.line2.setMinimumSize(QSize(1, 1))
        self.line2.setFont(font1)
        self.line2.setLayoutDirection(Qt.LeftToRight)
        self.line2.setFrameShadow(QFrame.Plain)
        self.line2.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line2, 3, 0, 1, 2)

        self.currentConditionsTextEdit = QTextEdit(self.centralwidget)
        self.currentConditionsTextEdit.setObjectName("currentConditionsTextEdit")
        sizePolicy3.setHeightForWidth(
            self.currentConditionsTextEdit.sizePolicy().hasHeightForWidth()
        )
        self.currentConditionsTextEdit.setSizePolicy(sizePolicy3)
        self.currentConditionsTextEdit.setMinimumSize(QSize(410, 90))
        self.currentConditionsTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.currentConditionsTextEdit.setFont(font1)
        self.currentConditionsTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.currentConditionsTextEdit.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )
        self.currentConditionsTextEdit.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustIgnored
        )
        self.currentConditionsTextEdit.setTabChangesFocus(True)
        self.currentConditionsTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.mainApp.addWidget(self.currentConditionsTextEdit, 20, 1, 1, 1)

        self.line13 = QFrame(self.centralwidget)
        self.line13.setObjectName("line13")
        sizePolicy1.setHeightForWidth(self.line13.sizePolicy().hasHeightForWidth())
        self.line13.setSizePolicy(sizePolicy1)
        self.line13.setMinimumSize(QSize(1, 1))
        self.line13.setFont(font1)
        self.line13.setLayoutDirection(Qt.LeftToRight)
        self.line13.setFrameShadow(QFrame.Plain)
        self.line13.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line13, 27, 0, 1, 2)

        self.heightLineEdit = QLineEdit(self.centralwidget)
        self.heightLineEdit.setObjectName("heightLineEdit")
        sizePolicy3.setHeightForWidth(
            self.heightLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.heightLineEdit.setSizePolicy(sizePolicy3)
        self.heightLineEdit.setMinimumSize(QSize(410, 0))
        self.heightLineEdit.setFont(font1)

        self.mainApp.addWidget(self.heightLineEdit, 12, 1, 1, 1)

        self.reasonForReferralLabel = QLabel(self.centralwidget)
        self.reasonForReferralLabel.setObjectName("reasonForReferralLabel")
        sizePolicy2.setHeightForWidth(
            self.reasonForReferralLabel.sizePolicy().hasHeightForWidth()
        )
        self.reasonForReferralLabel.setSizePolicy(sizePolicy2)
        self.reasonForReferralLabel.setMinimumSize(QSize(230, 0))
        self.reasonForReferralLabel.setFont(font1)

        self.mainApp.addWidget(self.reasonForReferralLabel, 30, 0, 1, 1)

        self.doctorProviderNumberLineEdit = QLineEdit(self.centralwidget)
        self.doctorProviderNumberLineEdit.setObjectName("doctorProviderNumberLineEdit")
        sizePolicy3.setHeightForWidth(
            self.doctorProviderNumberLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.doctorProviderNumberLineEdit.setSizePolicy(sizePolicy3)
        self.doctorProviderNumberLineEdit.setMinimumSize(QSize(410, 0))
        self.doctorProviderNumberLineEdit.setFont(font1)

        self.mainApp.addWidget(self.doctorProviderNumberLineEdit, 26, 1, 1, 1)

        self.line5 = QFrame(self.centralwidget)
        self.line5.setObjectName("line5")
        sizePolicy1.setHeightForWidth(self.line5.sizePolicy().hasHeightForWidth())
        self.line5.setSizePolicy(sizePolicy1)
        self.line5.setMinimumSize(QSize(1, 1))
        self.line5.setFont(font1)
        self.line5.setLayoutDirection(Qt.LeftToRight)
        self.line5.setFrameShadow(QFrame.Plain)
        self.line5.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line5, 9, 0, 1, 2)

        self.line1 = QFrame(self.centralwidget)
        self.line1.setObjectName("line1")
        sizePolicy1.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy1)
        self.line1.setMinimumSize(QSize(1, 1))
        self.line1.setFont(font1)
        self.line1.setLayoutDirection(Qt.LeftToRight)
        self.line1.setFrameShadow(QFrame.Plain)
        self.line1.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line1, 1, 0, 1, 2)

        self.weightLabel = QLabel(self.centralwidget)
        self.weightLabel.setObjectName("weightLabel")
        sizePolicy2.setHeightForWidth(self.weightLabel.sizePolicy().hasHeightForWidth())
        self.weightLabel.setSizePolicy(sizePolicy2)
        self.weightLabel.setMinimumSize(QSize(230, 0))
        self.weightLabel.setFont(font1)

        self.mainApp.addWidget(self.weightLabel, 10, 0, 1, 1)

        self.requestDateLabel = QLabel(self.centralwidget)
        self.requestDateLabel.setObjectName("requestDateLabel")
        sizePolicy2.setHeightForWidth(
            self.requestDateLabel.sizePolicy().hasHeightForWidth()
        )
        self.requestDateLabel.setSizePolicy(sizePolicy2)
        self.requestDateLabel.setMinimumSize(QSize(230, 0))
        self.requestDateLabel.setFont(font1)

        self.mainApp.addWidget(self.requestDateLabel, 32, 0, 1, 1)

        self.line7 = QFrame(self.centralwidget)
        self.line7.setObjectName("line7")
        sizePolicy1.setHeightForWidth(self.line7.sizePolicy().hasHeightForWidth())
        self.line7.setSizePolicy(sizePolicy1)
        self.line7.setMinimumSize(QSize(1, 1))
        self.line7.setFont(font1)
        self.line7.setLayoutDirection(Qt.LeftToRight)
        self.line7.setFrameShadow(QFrame.Plain)
        self.line7.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line7, 13, 0, 1, 2)

        self.line11 = QFrame(self.centralwidget)
        self.line11.setObjectName("line11")
        sizePolicy1.setHeightForWidth(self.line11.sizePolicy().hasHeightForWidth())
        self.line11.setSizePolicy(sizePolicy1)
        self.line11.setMinimumSize(QSize(1, 1))
        self.line11.setFont(font1)
        self.line11.setLayoutDirection(Qt.LeftToRight)
        self.line11.setFrameShadow(QFrame.Plain)
        self.line11.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line11, 21, 0, 1, 2)

        self.doctorFullNameLineEdit = QLineEdit(self.centralwidget)
        self.doctorFullNameLineEdit.setObjectName("doctorFullNameLineEdit")
        sizePolicy3.setHeightForWidth(
            self.doctorFullNameLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.doctorFullNameLineEdit.setSizePolicy(sizePolicy3)
        self.doctorFullNameLineEdit.setMinimumSize(QSize(410, 0))
        self.doctorFullNameLineEdit.setFont(font1)

        self.mainApp.addWidget(self.doctorFullNameLineEdit, 24, 1, 1, 1)

        self.fullNameLabel = QLabel(self.centralwidget)
        self.fullNameLabel.setObjectName("fullNameLabel")
        sizePolicy2.setHeightForWidth(
            self.fullNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.fullNameLabel.setSizePolicy(sizePolicy2)
        self.fullNameLabel.setMinimumSize(QSize(230, 0))
        self.fullNameLabel.setFont(font1)

        self.mainApp.addWidget(self.fullNameLabel, 2, 0, 1, 1)

        self.heightLabel = QLabel(self.centralwidget)
        self.heightLabel.setObjectName("heightLabel")
        sizePolicy2.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy2)
        self.heightLabel.setMinimumSize(QSize(230, 0))
        self.heightLabel.setFont(font1)

        self.mainApp.addWidget(self.heightLabel, 12, 0, 1, 1)

        self.doctorFullNameLabel = QLabel(self.centralwidget)
        self.doctorFullNameLabel.setObjectName("doctorFullNameLabel")
        sizePolicy2.setHeightForWidth(
            self.doctorFullNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.doctorFullNameLabel.setSizePolicy(sizePolicy2)
        self.doctorFullNameLabel.setMinimumSize(QSize(230, 0))
        self.doctorFullNameLabel.setFont(font1)

        self.mainApp.addWidget(self.doctorFullNameLabel, 24, 0, 1, 1)

        self.medicareNumberLineEdit = QLineEdit(self.centralwidget)
        self.medicareNumberLineEdit.setObjectName("medicareNumberLineEdit")
        sizePolicy3.setHeightForWidth(
            self.medicareNumberLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.medicareNumberLineEdit.setSizePolicy(sizePolicy3)
        self.medicareNumberLineEdit.setMinimumSize(QSize(410, 0))
        self.medicareNumberLineEdit.setFont(font1)

        self.mainApp.addWidget(self.medicareNumberLineEdit, 8, 1, 1, 1)

        self.requestDateDateEdit = QDateEdit(self.centralwidget)
        self.requestDateDateEdit.setObjectName("requestDateDateEdit")
        sizePolicy3.setHeightForWidth(
            self.requestDateDateEdit.sizePolicy().hasHeightForWidth()
        )
        self.requestDateDateEdit.setSizePolicy(sizePolicy3)
        self.requestDateDateEdit.setMinimumSize(QSize(410, 0))
        self.requestDateDateEdit.setFont(font1)
        self.requestDateDateEdit.setCalendarPopup(True)

        self.mainApp.addWidget(self.requestDateDateEdit, 32, 1, 1, 1)

        self.fullNameLineEdit = QLineEdit(self.centralwidget)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        sizePolicy3.setHeightForWidth(
            self.fullNameLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.fullNameLineEdit.setSizePolicy(sizePolicy3)
        self.fullNameLineEdit.setMinimumSize(QSize(410, 0))
        self.fullNameLineEdit.setFont(font1)

        self.mainApp.addWidget(self.fullNameLineEdit, 2, 1, 1, 1)

        self.weightLineEdit = QLineEdit(self.centralwidget)
        self.weightLineEdit.setObjectName("weightLineEdit")
        sizePolicy3.setHeightForWidth(
            self.weightLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.weightLineEdit.setSizePolicy(sizePolicy3)
        self.weightLineEdit.setMinimumSize(QSize(410, 0))
        self.weightLineEdit.setFont(font1)

        self.mainApp.addWidget(self.weightLineEdit, 10, 1, 1, 1)

        self.line15 = QFrame(self.centralwidget)
        self.line15.setObjectName("line15")
        sizePolicy1.setHeightForWidth(self.line15.sizePolicy().hasHeightForWidth())
        self.line15.setSizePolicy(sizePolicy1)
        self.line15.setMinimumSize(QSize(1, 1))
        self.line15.setFont(font1)
        self.line15.setLayoutDirection(Qt.LeftToRight)
        self.line15.setFrameShadow(QFrame.Plain)
        self.line15.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line15, 31, 0, 1, 2)

        self.line8 = QFrame(self.centralwidget)
        self.line8.setObjectName("line8")
        sizePolicy1.setHeightForWidth(self.line8.sizePolicy().hasHeightForWidth())
        self.line8.setSizePolicy(sizePolicy1)
        self.line8.setMinimumSize(QSize(1, 1))
        self.line8.setFont(font1)
        self.line8.setLayoutDirection(Qt.LeftToRight)
        self.line8.setFrameShadow(QFrame.Plain)
        self.line8.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line8, 15, 0, 1, 2)

        self.line4 = QFrame(self.centralwidget)
        self.line4.setObjectName("line4")
        sizePolicy1.setHeightForWidth(self.line4.sizePolicy().hasHeightForWidth())
        self.line4.setSizePolicy(sizePolicy1)
        self.line4.setMinimumSize(QSize(1, 1))
        self.line4.setFont(font1)
        self.line4.setLayoutDirection(Qt.LeftToRight)
        self.line4.setFrameShadow(QFrame.Plain)
        self.line4.setFrameShape(QFrame.HLine)

        self.mainApp.addWidget(self.line4, 7, 0, 1, 2)

        self.doctorPreferredContactLabel = QLabel(self.centralwidget)
        self.doctorPreferredContactLabel.setObjectName("doctorPreferredContactLabel")
        sizePolicy2.setHeightForWidth(
            self.doctorPreferredContactLabel.sizePolicy().hasHeightForWidth()
        )
        self.doctorPreferredContactLabel.setSizePolicy(sizePolicy2)
        self.doctorPreferredContactLabel.setMinimumSize(QSize(230, 0))
        self.doctorPreferredContactLabel.setFont(font1)

        self.mainApp.addWidget(self.doctorPreferredContactLabel, 28, 0, 1, 1)

        self.currentConditionsLabel = QLabel(self.centralwidget)
        self.currentConditionsLabel.setObjectName("currentConditionsLabel")
        sizePolicy2.setHeightForWidth(
            self.currentConditionsLabel.sizePolicy().hasHeightForWidth()
        )
        self.currentConditionsLabel.setSizePolicy(sizePolicy2)
        self.currentConditionsLabel.setMinimumSize(QSize(230, 0))
        self.currentConditionsLabel.setFont(font1)

        self.mainApp.addWidget(self.currentConditionsLabel, 20, 0, 1, 1)

        self.creatineLabel = QLabel(self.centralwidget)
        self.creatineLabel.setObjectName("creatineLabel")
        sizePolicy2.setHeightForWidth(
            self.creatineLabel.sizePolicy().hasHeightForWidth()
        )
        self.creatineLabel.setSizePolicy(sizePolicy2)
        self.creatineLabel.setMinimumSize(QSize(230, 0))
        self.creatineLabel.setFont(font1)

        self.mainApp.addWidget(self.creatineLabel, 16, 0, 1, 1)

        self.mainApp.setColumnStretch(0, 1)
        self.mainApp.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.mainApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        # if QT_CONFIG(shortcut)
        self.bloodPressureLabel.setBuddy(self.bloodPressureLineEdit)
        self.addressLabel.setBuddy(self.addressLineEdit)
        self.medicationsLabel.setBuddy(self.currentConditionsTextEdit)
        self.doctorProviderNumberLabel.setBuddy(self.doctorProviderNumberLineEdit)
        self.medicareNumberLabel.setBuddy(self.medicareNumberLineEdit)
        self.crClLabel.setBuddy(self.crClLineEdit)
        self.dOBLabel.setBuddy(self.dOBDateEdit)
        self.reasonForReferralLabel.setBuddy(self.reasonForReferralLineEdit)
        self.weightLabel.setBuddy(self.weightLineEdit)
        self.requestDateLabel.setBuddy(self.requestDateDateEdit)
        self.fullNameLabel.setBuddy(self.fullNameLineEdit)
        self.heightLabel.setBuddy(self.heightLineEdit)
        self.doctorFullNameLabel.setBuddy(self.doctorFullNameLineEdit)
        self.doctorPreferredContactLabel.setBuddy(self.doctorPreferredContactLineEdit)
        self.currentConditionsLabel.setBuddy(self.currentConditionsTextEdit)
        self.creatineLabel.setBuddy(self.creatineLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.fullNameLineEdit, self.dOBDateEdit)
        QWidget.setTabOrder(self.dOBDateEdit, self.addressLineEdit)
        QWidget.setTabOrder(self.addressLineEdit, self.medicareNumberLineEdit)
        QWidget.setTabOrder(self.medicareNumberLineEdit, self.weightLineEdit)
        QWidget.setTabOrder(self.weightLineEdit, self.heightLineEdit)
        QWidget.setTabOrder(self.heightLineEdit, self.bloodPressureLineEdit)
        QWidget.setTabOrder(self.bloodPressureLineEdit, self.creatineLineEdit)
        QWidget.setTabOrder(self.creatineLineEdit, self.crClLineEdit)
        QWidget.setTabOrder(self.crClLineEdit, self.currentConditionsTextEdit)
        QWidget.setTabOrder(self.currentConditionsTextEdit, self.doctorFullNameLineEdit)
        QWidget.setTabOrder(
            self.doctorFullNameLineEdit, self.doctorProviderNumberLineEdit
        )
        QWidget.setTabOrder(
            self.doctorProviderNumberLineEdit, self.doctorPreferredContactLineEdit
        )
        QWidget.setTabOrder(
            self.doctorPreferredContactLineEdit, self.reasonForReferralLineEdit
        )
        QWidget.setTabOrder(self.reasonForReferralLineEdit, self.requestDateDateEdit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.bloodPressureLabel.setText(
            QCoreApplication.translate("MainWindow", "Blood Pressure", None)
        )
        self.getInformationButton.setText(
            QCoreApplication.translate("MainWindow", "Populate Fields", None)
        )
        self.createDocumentButton.setText(
            QCoreApplication.translate("MainWindow", "Create Document", None)
        )
        self.TitleText.setText(
            QCoreApplication.translate("MainWindow", "DMMR Report Generator", None)
        )
        self.addressLabel.setText(
            QCoreApplication.translate("MainWindow", "Address", None)
        )
        self.medicationsLabel.setText(
            QCoreApplication.translate("MainWindow", "Medications", None)
        )
        self.doctorProviderNumberLabel.setText(
            QCoreApplication.translate("MainWindow", "Doctor Provider Number", None)
        )
        self.medicareNumberLabel.setText(
            QCoreApplication.translate("MainWindow", "Medicare Number", None)
        )
        self.crClLabel.setText(QCoreApplication.translate("MainWindow", "CrCl", None))
        self.dOBLabel.setText(QCoreApplication.translate("MainWindow", "DOB", None))
        self.reasonForReferralLabel.setText(
            QCoreApplication.translate("MainWindow", "Reason for Referral", None)
        )
        self.weightLabel.setText(
            QCoreApplication.translate("MainWindow", "Weight", None)
        )
        self.requestDateLabel.setText(
            QCoreApplication.translate("MainWindow", "Request Date", None)
        )
        self.fullNameLabel.setText(
            QCoreApplication.translate("MainWindow", "Full Name", None)
        )
        self.heightLabel.setText(
            QCoreApplication.translate("MainWindow", "Height", None)
        )
        self.doctorFullNameLabel.setText(
            QCoreApplication.translate("MainWindow", "Doctor Full name", None)
        )
        self.doctorPreferredContactLabel.setText(
            QCoreApplication.translate("MainWindow", "Doctor Preferred Contact", None)
        )
        self.currentConditionsLabel.setText(
            QCoreApplication.translate("MainWindow", "Current Conditions", None)
        )
        self.creatineLabel.setText(
            QCoreApplication.translate("MainWindow", "Creatine", None)
        )

    # retranslateUi
