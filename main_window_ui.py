# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(700, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 1000))
        MainWindow.setMaximumSize(QSize(700, 1000))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1000, 1000))
        self.centralwidget.setFocusPolicy(Qt.ClickFocus)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(480, 0, 221, 101))
        self.verticalLayout = QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setSpacing(22)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.CreateDoc = QPushButton(self.gridLayoutWidget)
        self.CreateDoc.setObjectName(u"CreateDoc")

        self.verticalLayout.addWidget(self.CreateDoc)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 100, 701, 901))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.doctorFullNameLabel = QLabel(self.gridLayoutWidget_2)
        self.doctorFullNameLabel.setObjectName(u"doctorFullNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doctorFullNameLabel.sizePolicy().hasHeightForWidth())
        self.doctorFullNameLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.doctorFullNameLabel, 23, 0, 1, 1)

        self.doctorProviderNumberLabel = QLabel(self.gridLayoutWidget_2)
        self.doctorProviderNumberLabel.setObjectName(u"doctorProviderNumberLabel")
        sizePolicy1.setHeightForWidth(self.doctorProviderNumberLabel.sizePolicy().hasHeightForWidth())
        self.doctorProviderNumberLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.doctorProviderNumberLabel, 25, 0, 1, 1)

        self.line14 = QFrame(self.gridLayoutWidget_2)
        self.line14.setObjectName(u"line14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line14.sizePolicy().hasHeightForWidth())
        self.line14.setSizePolicy(sizePolicy2)
        self.line14.setLayoutDirection(Qt.LeftToRight)
        self.line14.setFrameShape(QFrame.HLine)
        self.line14.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line14, 28, 0, 1, 2)

        self.line11 = QFrame(self.gridLayoutWidget_2)
        self.line11.setObjectName(u"line11")
        sizePolicy2.setHeightForWidth(self.line11.sizePolicy().hasHeightForWidth())
        self.line11.setSizePolicy(sizePolicy2)
        self.line11.setLayoutDirection(Qt.LeftToRight)
        self.line11.setFrameShape(QFrame.HLine)
        self.line11.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line11, 20, 0, 1, 2)

        self.heightLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        sizePolicy2.setHeightForWidth(self.heightLineEdit.sizePolicy().hasHeightForWidth())
        self.heightLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.heightLineEdit, 11, 1, 1, 1)

        self.line7 = QFrame(self.gridLayoutWidget_2)
        self.line7.setObjectName(u"line7")
        sizePolicy2.setHeightForWidth(self.line7.sizePolicy().hasHeightForWidth())
        self.line7.setSizePolicy(sizePolicy2)
        self.line7.setLayoutDirection(Qt.LeftToRight)
        self.line7.setFrameShape(QFrame.HLine)
        self.line7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line7, 12, 0, 1, 2)

        self.line3 = QFrame(self.gridLayoutWidget_2)
        self.line3.setObjectName(u"line3")
        sizePolicy2.setHeightForWidth(self.line3.sizePolicy().hasHeightForWidth())
        self.line3.setSizePolicy(sizePolicy2)
        self.line3.setLayoutDirection(Qt.LeftToRight)
        self.line3.setFrameShape(QFrame.HLine)
        self.line3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line3, 4, 0, 1, 2)

        self.line2 = QFrame(self.gridLayoutWidget_2)
        self.line2.setObjectName(u"line2")
        sizePolicy2.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy2)
        self.line2.setLayoutDirection(Qt.LeftToRight)
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line2, 2, 0, 1, 2)

        self.addressLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        sizePolicy2.setHeightForWidth(self.addressLineEdit.sizePolicy().hasHeightForWidth())
        self.addressLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.addressLineEdit, 5, 1, 1, 1)

        self.dOBLabel = QLabel(self.gridLayoutWidget_2)
        self.dOBLabel.setObjectName(u"dOBLabel")
        sizePolicy1.setHeightForWidth(self.dOBLabel.sizePolicy().hasHeightForWidth())
        self.dOBLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.dOBLabel, 3, 0, 1, 1)

        self.currentConditionsTextEdit = QTextEdit(self.gridLayoutWidget_2)
        self.currentConditionsTextEdit.setObjectName(u"currentConditionsTextEdit")
        sizePolicy2.setHeightForWidth(self.currentConditionsTextEdit.sizePolicy().hasHeightForWidth())
        self.currentConditionsTextEdit.setSizePolicy(sizePolicy2)
        self.currentConditionsTextEdit.setMaximumSize(QSize(16777215, 125))
        self.currentConditionsTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.currentConditionsTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.currentConditionsTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.currentConditionsTextEdit.setTabChangesFocus(True)
        self.currentConditionsTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout.addWidget(self.currentConditionsTextEdit, 19, 1, 1, 1)

        self.doctorPreferredContactLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.doctorPreferredContactLineEdit.setObjectName(u"doctorPreferredContactLineEdit")
        sizePolicy2.setHeightForWidth(self.doctorPreferredContactLineEdit.sizePolicy().hasHeightForWidth())
        self.doctorPreferredContactLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.doctorPreferredContactLineEdit, 27, 1, 1, 1)

        self.requestDateLabel = QLabel(self.gridLayoutWidget_2)
        self.requestDateLabel.setObjectName(u"requestDateLabel")
        sizePolicy1.setHeightForWidth(self.requestDateLabel.sizePolicy().hasHeightForWidth())
        self.requestDateLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.requestDateLabel, 31, 0, 1, 1)

        self.addressLabel = QLabel(self.gridLayoutWidget_2)
        self.addressLabel.setObjectName(u"addressLabel")
        sizePolicy1.setHeightForWidth(self.addressLabel.sizePolicy().hasHeightForWidth())
        self.addressLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.addressLabel, 5, 0, 1, 1)

        self.fullNameLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.fullNameLineEdit.setObjectName(u"fullNameLineEdit")
        sizePolicy2.setHeightForWidth(self.fullNameLineEdit.sizePolicy().hasHeightForWidth())
        self.fullNameLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.fullNameLineEdit, 1, 1, 1, 1)

        self.reasonForReferralLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.reasonForReferralLineEdit.setObjectName(u"reasonForReferralLineEdit")
        sizePolicy2.setHeightForWidth(self.reasonForReferralLineEdit.sizePolicy().hasHeightForWidth())
        self.reasonForReferralLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.reasonForReferralLineEdit, 29, 1, 1, 1)

        self.creatineLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.creatineLineEdit.setObjectName(u"creatineLineEdit")
        sizePolicy2.setHeightForWidth(self.creatineLineEdit.sizePolicy().hasHeightForWidth())
        self.creatineLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.creatineLineEdit, 15, 1, 1, 1)

        self.doctorFullNameLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.doctorFullNameLineEdit.setObjectName(u"doctorFullNameLineEdit")
        sizePolicy2.setHeightForWidth(self.doctorFullNameLineEdit.sizePolicy().hasHeightForWidth())
        self.doctorFullNameLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.doctorFullNameLineEdit, 23, 1, 1, 1)

        self.line6 = QFrame(self.gridLayoutWidget_2)
        self.line6.setObjectName(u"line6")
        sizePolicy2.setHeightForWidth(self.line6.sizePolicy().hasHeightForWidth())
        self.line6.setSizePolicy(sizePolicy2)
        self.line6.setLayoutDirection(Qt.LeftToRight)
        self.line6.setFrameShape(QFrame.HLine)
        self.line6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line6, 10, 0, 1, 2)

        self.bloodPressureLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.bloodPressureLineEdit.setObjectName(u"bloodPressureLineEdit")
        sizePolicy2.setHeightForWidth(self.bloodPressureLineEdit.sizePolicy().hasHeightForWidth())
        self.bloodPressureLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.bloodPressureLineEdit, 13, 1, 1, 1)

        self.line10 = QFrame(self.gridLayoutWidget_2)
        self.line10.setObjectName(u"line10")
        sizePolicy2.setHeightForWidth(self.line10.sizePolicy().hasHeightForWidth())
        self.line10.setSizePolicy(sizePolicy2)
        self.line10.setLayoutDirection(Qt.LeftToRight)
        self.line10.setFrameShape(QFrame.HLine)
        self.line10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line10, 18, 0, 1, 2)

        self.currentConditionsLabel = QLabel(self.gridLayoutWidget_2)
        self.currentConditionsLabel.setObjectName(u"currentConditionsLabel")
        sizePolicy1.setHeightForWidth(self.currentConditionsLabel.sizePolicy().hasHeightForWidth())
        self.currentConditionsLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.currentConditionsLabel, 19, 0, 1, 1)

        self.line9 = QFrame(self.gridLayoutWidget_2)
        self.line9.setObjectName(u"line9")
        sizePolicy2.setHeightForWidth(self.line9.sizePolicy().hasHeightForWidth())
        self.line9.setSizePolicy(sizePolicy2)
        self.line9.setLayoutDirection(Qt.LeftToRight)
        self.line9.setFrameShape(QFrame.HLine)
        self.line9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line9, 16, 0, 1, 2)

        self.line13 = QFrame(self.gridLayoutWidget_2)
        self.line13.setObjectName(u"line13")
        sizePolicy2.setHeightForWidth(self.line13.sizePolicy().hasHeightForWidth())
        self.line13.setSizePolicy(sizePolicy2)
        self.line13.setLayoutDirection(Qt.LeftToRight)
        self.line13.setFrameShape(QFrame.HLine)
        self.line13.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line13, 26, 0, 1, 2)

        self.heightLabel = QLabel(self.gridLayoutWidget_2)
        self.heightLabel.setObjectName(u"heightLabel")
        sizePolicy1.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.heightLabel, 11, 0, 1, 1)

        self.line4 = QFrame(self.gridLayoutWidget_2)
        self.line4.setObjectName(u"line4")
        sizePolicy2.setHeightForWidth(self.line4.sizePolicy().hasHeightForWidth())
        self.line4.setSizePolicy(sizePolicy2)
        self.line4.setLayoutDirection(Qt.LeftToRight)
        self.line4.setFrameShape(QFrame.HLine)
        self.line4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line4, 6, 0, 1, 2)

        self.crClLabel = QLabel(self.gridLayoutWidget_2)
        self.crClLabel.setObjectName(u"crClLabel")
        sizePolicy1.setHeightForWidth(self.crClLabel.sizePolicy().hasHeightForWidth())
        self.crClLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.crClLabel, 17, 0, 1, 1)

        self.medicareNumberLabel = QLabel(self.gridLayoutWidget_2)
        self.medicareNumberLabel.setObjectName(u"medicareNumberLabel")
        sizePolicy1.setHeightForWidth(self.medicareNumberLabel.sizePolicy().hasHeightForWidth())
        self.medicareNumberLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.medicareNumberLabel, 7, 0, 1, 1)

        self.line1 = QFrame(self.gridLayoutWidget_2)
        self.line1.setObjectName(u"line1")
        sizePolicy2.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy2)
        self.line1.setLayoutDirection(Qt.LeftToRight)
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line1, 0, 0, 1, 2)

        self.weightLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        sizePolicy2.setHeightForWidth(self.weightLineEdit.sizePolicy().hasHeightForWidth())
        self.weightLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.weightLineEdit, 9, 1, 1, 1)

        self.doctorProviderNumberLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.doctorProviderNumberLineEdit.setObjectName(u"doctorProviderNumberLineEdit")
        sizePolicy2.setHeightForWidth(self.doctorProviderNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.doctorProviderNumberLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.doctorProviderNumberLineEdit, 25, 1, 1, 1)

        self.reasonForReferralLabel = QLabel(self.gridLayoutWidget_2)
        self.reasonForReferralLabel.setObjectName(u"reasonForReferralLabel")
        sizePolicy1.setHeightForWidth(self.reasonForReferralLabel.sizePolicy().hasHeightForWidth())
        self.reasonForReferralLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.reasonForReferralLabel, 29, 0, 1, 1)

        self.requestDateDateEdit = QDateEdit(self.gridLayoutWidget_2)
        self.requestDateDateEdit.setObjectName(u"requestDateDateEdit")
        sizePolicy2.setHeightForWidth(self.requestDateDateEdit.sizePolicy().hasHeightForWidth())
        self.requestDateDateEdit.setSizePolicy(sizePolicy2)
        self.requestDateDateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.requestDateDateEdit, 31, 1, 1, 1)

        self.dOBDateEdit = QDateEdit(self.gridLayoutWidget_2)
        self.dOBDateEdit.setObjectName(u"dOBDateEdit")
        sizePolicy2.setHeightForWidth(self.dOBDateEdit.sizePolicy().hasHeightForWidth())
        self.dOBDateEdit.setSizePolicy(sizePolicy2)
        self.dOBDateEdit.setWrapping(False)
        self.dOBDateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dOBDateEdit.setProperty("showGroupSeparator", False)
        self.dOBDateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dOBDateEdit, 3, 1, 1, 1)

        self.crClLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.crClLineEdit.setObjectName(u"crClLineEdit")
        sizePolicy2.setHeightForWidth(self.crClLineEdit.sizePolicy().hasHeightForWidth())
        self.crClLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.crClLineEdit, 17, 1, 1, 1)

        self.doctorPreferredContactLabel = QLabel(self.gridLayoutWidget_2)
        self.doctorPreferredContactLabel.setObjectName(u"doctorPreferredContactLabel")
        sizePolicy1.setHeightForWidth(self.doctorPreferredContactLabel.sizePolicy().hasHeightForWidth())
        self.doctorPreferredContactLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.doctorPreferredContactLabel, 27, 0, 1, 1)

        self.weightLabel = QLabel(self.gridLayoutWidget_2)
        self.weightLabel.setObjectName(u"weightLabel")
        sizePolicy1.setHeightForWidth(self.weightLabel.sizePolicy().hasHeightForWidth())
        self.weightLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.weightLabel, 9, 0, 1, 1)

        self.fullNameLabel = QLabel(self.gridLayoutWidget_2)
        self.fullNameLabel.setObjectName(u"fullNameLabel")
        sizePolicy1.setHeightForWidth(self.fullNameLabel.sizePolicy().hasHeightForWidth())
        self.fullNameLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fullNameLabel, 1, 0, 1, 1)

        self.line5 = QFrame(self.gridLayoutWidget_2)
        self.line5.setObjectName(u"line5")
        sizePolicy2.setHeightForWidth(self.line5.sizePolicy().hasHeightForWidth())
        self.line5.setSizePolicy(sizePolicy2)
        self.line5.setLayoutDirection(Qt.LeftToRight)
        self.line5.setFrameShape(QFrame.HLine)
        self.line5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line5, 8, 0, 1, 2)

        self.line8 = QFrame(self.gridLayoutWidget_2)
        self.line8.setObjectName(u"line8")
        sizePolicy2.setHeightForWidth(self.line8.sizePolicy().hasHeightForWidth())
        self.line8.setSizePolicy(sizePolicy2)
        self.line8.setLayoutDirection(Qt.LeftToRight)
        self.line8.setFrameShape(QFrame.HLine)
        self.line8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line8, 14, 0, 1, 2)

        self.line16 = QFrame(self.gridLayoutWidget_2)
        self.line16.setObjectName(u"line16")
        sizePolicy2.setHeightForWidth(self.line16.sizePolicy().hasHeightForWidth())
        self.line16.setSizePolicy(sizePolicy2)
        self.line16.setLayoutDirection(Qt.LeftToRight)
        self.line16.setFrameShape(QFrame.HLine)
        self.line16.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line16, 32, 0, 1, 2)

        self.medicareNumberLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.medicareNumberLineEdit.setObjectName(u"medicareNumberLineEdit")
        sizePolicy2.setHeightForWidth(self.medicareNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.medicareNumberLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.medicareNumberLineEdit, 7, 1, 1, 1)

        self.creatineLabel = QLabel(self.gridLayoutWidget_2)
        self.creatineLabel.setObjectName(u"creatineLabel")
        sizePolicy1.setHeightForWidth(self.creatineLabel.sizePolicy().hasHeightForWidth())
        self.creatineLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.creatineLabel, 15, 0, 1, 1)

        self.line12 = QFrame(self.gridLayoutWidget_2)
        self.line12.setObjectName(u"line12")
        sizePolicy2.setHeightForWidth(self.line12.sizePolicy().hasHeightForWidth())
        self.line12.setSizePolicy(sizePolicy2)
        self.line12.setLayoutDirection(Qt.LeftToRight)
        self.line12.setFrameShape(QFrame.HLine)
        self.line12.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line12, 24, 0, 1, 2)

        self.line15 = QFrame(self.gridLayoutWidget_2)
        self.line15.setObjectName(u"line15")
        sizePolicy2.setHeightForWidth(self.line15.sizePolicy().hasHeightForWidth())
        self.line15.setSizePolicy(sizePolicy2)
        self.line15.setLayoutDirection(Qt.LeftToRight)
        self.line15.setFrameShape(QFrame.HLine)
        self.line15.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line15, 30, 0, 1, 2)

        self.bloodPressureLabel = QLabel(self.gridLayoutWidget_2)
        self.bloodPressureLabel.setObjectName(u"bloodPressureLabel")
        sizePolicy1.setHeightForWidth(self.bloodPressureLabel.sizePolicy().hasHeightForWidth())
        self.bloodPressureLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.bloodPressureLabel, 13, 0, 1, 1)

        self.medicationsLabel = QLabel(self.gridLayoutWidget_2)
        self.medicationsLabel.setObjectName(u"medicationsLabel")
        sizePolicy1.setHeightForWidth(self.medicationsLabel.sizePolicy().hasHeightForWidth())
        self.medicationsLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.medicationsLabel, 21, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableView = QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.addRowPushButton = QPushButton(self.gridLayoutWidget_2)
        self.addRowPushButton.setObjectName(u"addRowPushButton")

        self.verticalLayout_3.addWidget(self.addRowPushButton)

        self.removeRowPushButton = QPushButton(self.gridLayoutWidget_2)
        self.removeRowPushButton.setObjectName(u"removeRowPushButton")

        self.verticalLayout_3.addWidget(self.removeRowPushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout, 22, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.doctorFullNameLabel.setBuddy(self.doctorFullNameLineEdit)
        self.doctorProviderNumberLabel.setBuddy(self.doctorProviderNumberLineEdit)
        self.dOBLabel.setBuddy(self.dOBDateEdit)
        self.requestDateLabel.setBuddy(self.requestDateDateEdit)
        self.addressLabel.setBuddy(self.addressLineEdit)
        self.currentConditionsLabel.setBuddy(self.currentConditionsTextEdit)
        self.heightLabel.setBuddy(self.heightLineEdit)
        self.crClLabel.setBuddy(self.crClLineEdit)
        self.medicareNumberLabel.setBuddy(self.medicareNumberLineEdit)
        self.reasonForReferralLabel.setBuddy(self.reasonForReferralLineEdit)
        self.doctorPreferredContactLabel.setBuddy(self.doctorPreferredContactLineEdit)
        self.weightLabel.setBuddy(self.weightLineEdit)
        self.fullNameLabel.setBuddy(self.fullNameLineEdit)
        self.creatineLabel.setBuddy(self.creatineLineEdit)
        self.bloodPressureLabel.setBuddy(self.bloodPressureLineEdit)
        self.medicationsLabel.setBuddy(self.currentConditionsTextEdit)
#endif // QT_CONFIG(shortcut)
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
        QWidget.setTabOrder(self.doctorFullNameLineEdit, self.doctorProviderNumberLineEdit)
        QWidget.setTabOrder(self.doctorProviderNumberLineEdit, self.doctorPreferredContactLineEdit)
        QWidget.setTabOrder(self.doctorPreferredContactLineEdit, self.reasonForReferralLineEdit)
        QWidget.setTabOrder(self.reasonForReferralLineEdit, self.requestDateDateEdit)
        QWidget.setTabOrder(self.requestDateDateEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.CreateDoc)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CreateDoc.setText(QCoreApplication.translate("MainWindow", u"Create Document", None))
        self.doctorFullNameLabel.setText(QCoreApplication.translate("MainWindow", u"Doctor Full name", None))
        self.doctorProviderNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Doctor Provider Number", None))
        self.dOBLabel.setText(QCoreApplication.translate("MainWindow", u"DOB", None))
        self.requestDateLabel.setText(QCoreApplication.translate("MainWindow", u"Request Date", None))
        self.addressLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.currentConditionsLabel.setText(QCoreApplication.translate("MainWindow", u"Current Conditions", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.crClLabel.setText(QCoreApplication.translate("MainWindow", u"CrCl", None))
        self.medicareNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Medicare Number", None))
        self.reasonForReferralLabel.setText(QCoreApplication.translate("MainWindow", u"Reason for Referral", None))
        self.doctorPreferredContactLabel.setText(QCoreApplication.translate("MainWindow", u"Doctor Preferred Contact", None))
        self.weightLabel.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.fullNameLabel.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.creatineLabel.setText(QCoreApplication.translate("MainWindow", u"Creatine", None))
        self.bloodPressureLabel.setText(QCoreApplication.translate("MainWindow", u"Blood Pressure", None))
        self.medicationsLabel.setText(QCoreApplication.translate("MainWindow", u"Medications", None))
        self.addRowPushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.removeRowPushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

