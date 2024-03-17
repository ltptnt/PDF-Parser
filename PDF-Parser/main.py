import json
import os
import sys
import ctypes
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QDate, QTimer, Qt
from PySide6.QtGui import QIcon, QFontDatabase
from qt_material import apply_stylesheet

# Fix the import error
PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(PATH))
# set the os environment variable to scale the application.
# os.environ["QT_SCALE_FACTOR"] = "0.8"


# import the classes from the other files
from Parsing import create_document, parse
from main_window_ui import Ui_MainWindow
from Doctor import Doctor


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Set the app id for windows and set the icon
        myappid = "LP.Apps.PDF-Parser.v1.0"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Create the main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # set the window title and icon
        self.setWindowTitle("DMMR Report Generator")
        self.setWindowIcon(QIcon(PATH + "/resources/icon.png"))

        # format the application
        self.formatApp()

        # add the button events
        self.ui.loadFilesButton.clicked.connect(self.loadFile)
        self.ui.saveFilesButton.clicked.connect(self.saveFile)

        # add the dropdown menu options
        self.ui.runModeComboBox.addItems(["Single", "Bulk"])
        self.ui.runModeComboBox.currentIndexChanged.connect(self.runType)

        # init doctor to None
        self.doctors = []

        # Load the application settings
        self.loadSettings()

    def formatApp(self) -> None:
        # set the fonts and styles
        QFontDatabase.addApplicationFont(PATH + "resources/OpenSans-Regular.ttf")
        QFontDatabase.addApplicationFont(PATH + "resources/OpenSans-Light.ttf")
        apply_stylesheet(self, theme="light_blue.xml", extra={"density-scale": "-2.0"})

        # ---- fix formatting problems ------
        # set all the fonts to OpenSans Light
        self.ui.loadFilesButton.setStyleSheet(
            "font-family: 'OpenSans Light'; font-size: 13px;" + self.ui.loadFilesButton.styleSheet()
        )
        self.ui.saveFilesButton.setStyleSheet(
            "font-family: 'OpenSans Light'; font-size: 13px;" + self.ui.saveFilesButton.styleSheet()
        )
        # set the title font to OpenSans
        self.ui.titleText.setStyleSheet(
            "font-family: 'OpenSans'; font-size: 30px;" + self.ui.titleText.styleSheet()
        )
        # set the font for all the widgets
        for child in self.ui.centralwidget.children():
            if "button" not in child.objectName() and hasattr(child, "setStyleSheet"):
                child.setStyleSheet(
                    "font-family: 'OpenSans Light'; font-size: 16px; font-weight: 200;"
                    + child.styleSheet()
                )
        # Remove the indentation on the line and text edits
        for child in self.ui.centralwidget.children():
            if hasattr(child, "setStyleSheet") and ("LineEdit" in child.objectName() or "TextEdit" in child.objectName() or "DateEdit" in child.objectName()):
                child.setStyleSheet(
                    "padding: 2px; " + child.styleSheet()
                )

    def loadSettings(self) -> None:
        self.settings = {}
        if os.path.exists(PATH + "/settings.json"):
            with open(PATH + "/settings.json", "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        if (
            self.settings.get("openPath") is None
            or os.path.exists(self.settings.get("openPath")) is False
        ):
            self.settings["openPath"] = ""
        if (
            self.settings.get("savePath") is None
            or os.path.exists(self.settings.get("savePath")) is False
        ):
            self.settings["savePath"] = ""

    def _resize(self) -> None:
        self.resize(self.minimumSizeHint())

    def runType(self) -> None:
        if self.ui.runModeComboBox.currentText() == "Single":
            self.ui.loadFilesButton.setText("Load File")
            self.ui.saveFilesButton.setText("Create Document")
            for child in self.ui.centralwidget.children():
                if hasattr(child, "show"):
                    child.show()
        else:
            self.ui.loadFilesButton.setText("Load Files")
            self.ui.saveFilesButton.setText("Create Documents")

            # remove all the fields not in the title grid layout
            titleWidgetChildren = [
                titleWidgetChild.objectName()
                for titleWidgetChild in self.ui.titleWidget.children()
            ] + ["titleWidget", "gridLayout_3"]
            for child in self.ui.centralwidget.children():
                if child.objectName() not in titleWidgetChildren and hasattr(child, "hide"):
                    child.hide()
        _timer = QTimer()
        _timer.singleShot(30, self._resize)

    def populateFields(self) -> None:
        # Set the Doctor's information
        self.ui.doctorFullNameLineEdit.setText(self.doctors[0].get_name())
        self.ui.doctorProviderNumberLineEdit.setText(
            self.doctors[0].get_provider_number()
        )
        self.ui.doctorPreferredContactLineEdit.setText(
            self.doctors[0].get_pref_contact()
        )
        self.ui.reasonForReferralLineEdit.setText(
            self.doctors[0].get_reason_for_referral()
        )
        self.ui.requestDateDateEdit.setDate(
            QDate.fromString(self.doctors[0].get_request_time(), "dd/MM/yyyy")
        )

        # Set the Patient's information
        patient = self.doctors[0].get_patient()
        if patient is None:
            return
        self.ui.fullNameLineEdit.setText(patient.get_name())
        self.ui.dOBDateEdit.setDate(QDate.fromString(patient.get_dob(), "dd/MM/yyyy"))
        self.ui.addressLineEdit.setText(patient.get_address())
        self.ui.medicareNumberLineEdit.setText(patient.get_medicare())
        self.ui.weightLineEdit.setText(patient.get_weight())
        self.ui.heightLineEdit.setText(patient.get_height())
        self.ui.bloodPressureLineEdit.setText(patient.get_blood_pressure())
        self.ui.creatineLineEdit.setText(patient.get_creatine())
        self.ui.crClLineEdit.setText(patient.get_CrCl())
        conditions = patient.get_current_conditions()
        if type(conditions) is list:
            conditions = "\n".join(conditions)
            self.ui.currentConditionsTextEdit.setText(conditions)

        # Set the Medication information
        medications = patient.get_medications()
        # Display in format "Medication: Dosage"
        if type(medications) is dict:
            medications = "\n".join(
                [
                    f"{medication}: {dosage}"
                    for medication, dosage in medications.items()
                ]
            )
            self.ui.medicationsTextEdit.setText(medications)

    def updateData(self) -> None:
        if len(self.doctors) == 0 or self.doctors[0] is None:
            return
        self.doctors[0].set_name(self.ui.doctorFullNameLineEdit.text())
        self.doctors[0].set_provider_number(self.ui.doctorProviderNumberLineEdit.text())
        self.doctors[0].set_pref_contact(self.ui.doctorPreferredContactLineEdit.text())
        self.doctors[0].set_reason_for_referral(
            self.ui.reasonForReferralLineEdit.text()
        )
        if (
            self.doctors[0].get_request_time() is None
            and self.ui.requestDateDateEdit.date().toString("dd/MM/yyyy")
            != "01/01/2000"
        ):
            self.doctors[0].set_request_time(
                self.ui.requestDateDateEdit.date().toString("dd/MM/yyyy")
            )

        patient = self.doctors[0].get_patient()
        if patient is None:
            return

        patient.set_name(self.ui.fullNameLineEdit.text())
        patient.set_dob(self.ui.dOBDateEdit.date().toString("dd/MM/yyyy"))
        patient.set_address(self.ui.addressLineEdit.text())
        patient.set_medicare(self.ui.medicareNumberLineEdit.text())
        patient.set_weight(self.ui.weightLineEdit.text())
        patient.set_height(self.ui.heightLineEdit.text())
        patient.set_blood_pressure(self.ui.bloodPressureLineEdit.text())
        patient.set_creatine(self.ui.creatineLineEdit.text())
        patient.set_CrCl(self.ui.crClLineEdit.text())

        # Set the Current Conditions
        patient.set_current_conditions(
            self.ui.currentConditionsTextEdit.toPlainText().split("\n")
        )

        # Set the Medications
        medications = self.ui.medicationsTextEdit.toPlainText().split("\n")
        medications = [medication.split(":") for medication in medications]
        medications = {medication[0]: medication[1] for medication in medications}

        patient.set_medications(medications)
        self.doctors[0].set_patient(patient)

    def addDoctor(self, filesPath) -> Doctor:
        if filesPath is None:
            return
        self.doctors.append(parse(filesPath))

    def loadFile(self) -> None:
        options = QFileDialog.Options()
        if self.ui.runModeComboBox.currentText() == "Bulk":
            files = QFileDialog.getExistingDirectory(
                self, "Open Folder", self.settings["openPath"], options=options
            )
            if files:
                self.settings["openPath"] = files
                # get all the files in the directory
                files = [f"{files}/{file}" for file in os.listdir(files)]
                for file in files:
                    if file.endswith(".pdf"):
                        self.addDoctor(file)
        else:
            file, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                self.settings["openPath"],
                "PDF Files (*.pdf)",
                options=options,
            )
            if file:
                self.settings["openPath"] = file.rsplit("/", 1)[0]
                self.addDoctor(file)
                self.populateFields()
        # get path of current file and save the settings

        with open(PATH + "/settings.json", "w", encoding="utf-8") as f:
            json.dump(self.settings, f)

    def saveFile(self) -> None:
        options = QFileDialog.Options()
        if self.ui.runModeComboBox.currentText() == "Bulk":
            saveLocation = QFileDialog.getExistingDirectory(
                self, "Save Folder", self.settings["savePath"], options=options
            )
            if saveLocation:
                self.settings["savePath"] = saveLocation
                for doctor in self.doctors:
                    document = create_document(doctor)
                    # add checks to prevent overwriting files
                    if os.path.exists(
                        f"{saveLocation}/DMMR REPORT - {doctor.get_patient().get_name()}.docx"
                    ):
                        i = 1
                        while os.path.exists(
                            f"{saveLocation}/DMMR REPORT - {doctor.get_patient().get_name()}({i}).docx"
                        ):
                            i += 1
                        document.save(
                            f"{saveLocation}/DMMR REPORT - {doctor.get_patient().get_name()}({i}).docx"
                        )

                    else:
                        document.save(
                            f"{saveLocation}/DMMR REPORT - {doctor.get_patient().get_name()}.docx"
                        )

        else:
            if len(self.doctors) == 0:
                return
            saveLocation, _ = QFileDialog.getSaveFileName(
                self,
                "Save File",
                self.settings["savePath"]
                + "/DMMR REPORT - "
                + self.doctors[0].get_patient().get_name()
                + ".docx",
                "Word Document (*.docx)",
                options=options,
            )
            if saveLocation:
                self.settings["savePath"] = saveLocation.rsplit("/", 1)[0]
                self.updateData()
                document = create_document(self.doctors[0])
                document.save(saveLocation)
        with open(PATH + "/settings.json", "w", encoding="utf-8") as f:
            json.dump(self.settings, f)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(f"An error has occurred\n {exception}")
    msg.setWindowTitle("Error")
    msg.exec()

    # close the application on close
    app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # display exceptions as message boxes
    sys.excepthook = except_hook
    sys.exit(app.exec())
