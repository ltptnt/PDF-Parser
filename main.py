from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from Parsing import create_document, parse

# Import the Ui_MainWindow class from your generated file
from main_window_ui import Ui_MainWindow  # Make sure to replace 'your_generated_file' with the actual name of your Python file containing the Ui_MainWindow class
from Doctor import Doctor
from Patient import Patient
from qt_material import apply_stylesheet

from docx import Document



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Create the main window
        self.ui = Ui_MainWindow()

        self.filePath = None
        #apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True)
        self.setWindowTitle("DMMR Report")
        self.setWindowIcon(QIcon("resources/icon.png"))
        QFontDatabase.addApplicationFont("resources/OpenSans-Regular.ttf")
        QFontDatabase.addApplicationFont("resources/OpenSans-Light.ttf")
        self.ui.setupUi(self)

        # set the button events
        self.ui.createDocumentButton.clicked.connect(self.saveFile)
        self.ui.getInformationButton.clicked.connect(self.loadFile)

        # set the dropdown menu options
        self.ui.templateSelectorComboBox.addItems(["Template 1", "Template 2"])
        self.ui.templateSelectorComboBox.currentIndexChanged.connect(self.populateFields)

        # Set doctor to None
        self.doctor = Doctor()


    def populateFields(self) -> None:
        # Set the Doctor's information
        self.doctor = parse(self.filePath, self.ui.templateSelectorComboBox.currentIndex() + 1)

        self.ui.doctorFullNameLineEdit.setText(self.doctor.get_name())
        self.ui.doctorProviderNumberLineEdit.setText(self.doctor.get_provider_number())
        self.ui.doctorPreferredContactLineEdit.setText(self.doctor.get_pref_contact())
        self.ui.reasonForReferralLineEdit.setText(self.doctor.get_reason_for_referral())
        self.ui.requestDateDateEdit.setDate(QDate.fromString(self.doctor.get_request_time(), "dd/MM/yyyy"))

        # Set the Patient's information
        patient = self.doctor.get_patient()
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
        if type(conditions) == list:
            conditions = "\n".join(conditions)
            self.ui.currentConditionsTextEdit.setText(conditions)

        # Set the Medication information
        medications = patient.get_medications()
        # Display in format "Medication: Dosage"
        if type(medications) == dict:
            medications = "\n".join([f"{medication}: {dosage}" for medication, dosage in medications.items()])
            self.ui.medicationsTextEdit.setText(medications)

    def updateData(self) -> None:
        if self.doctor is None:
            return
        self.doctor.set_name(self.ui.doctorFullNameLineEdit.text())
        self.doctor.set_provider_number(self.ui.doctorProviderNumberLineEdit.text())
        self.doctor.set_pref_contact(self.ui.doctorPreferredContactLineEdit.text())
        self.doctor.set_reason_for_referral(self.ui.reasonForReferralLineEdit.text())
        if self.doctor.get_request_time() is None and self.ui.requestDateDateEdit.date().toString("dd/MM/yyyy") != "01/01/2000":
            self.doctor.set_request_time(self.ui.requestDateDateEdit.date().toString("dd/MM/yyyy"))

        patient = self.doctor.get_patient()
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
        patient.set_current_conditions(self.ui.currentConditionsTextEdit.toPlainText().split("\n"))

        # Set the Medications
        medications = self.ui.medicationsTextEdit.toPlainText().split("\n")
        medications = [medication.split(":") for medication in medications]
        medications = {medication[0]: medication[1] for medication in medications}

        patient.set_medications(medications)
        self.doctor.set_patient(patient)
    
    def loadFile(self) -> None:
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","PDF Files (*.pdf)", options=options)
        if fileName:
            print(fileName)
            self.filePath = fileName
            print("File Loaded")
        else:
            print("No file selected")
            self.filePath = "testing/example1.pdf"
        self.populateFields()

    def saveFile(self) -> None:
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File", "","Word Document (*.docx)", options=options)
        if fileName:
            print(fileName)
            self.filePath = fileName
            self.updateData()
            document = create_document(self.doctor)
            document.save(fileName)

            print("File Saved")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
