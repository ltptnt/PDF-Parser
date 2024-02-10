from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QDate
# Import the Ui_MainWindow class from your generated file
from main_window_ui import Ui_MainWindow  # Make sure to replace 'your_generated_file' with the actual name of your Python file containing the Ui_MainWindow class
from Doctor import Doctor
from Patient import Patient
from Parsing import parse
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filePath = 'example1.pdf'
        apply_stylesheet(app, theme='light_blue.xml')

        self.ui.CreateDoc.clicked.connect(self.createDocument)

    
    def populate_information(self, doctor: Doctor):
        # Set the Doctor's information
        self.ui.doctorFullNameLineEdit.setText(doctor.get_name())
        self.ui.doctorProviderNumberLineEdit.setText(doctor.get_provider_number())
        self.ui.doctorPreferredContactLineEdit.setText(doctor.get_pref_contact())
        self.ui.reasonForReferralLineEdit.setText(doctor.get_reason_for_referral())
        self.ui.requestDateDateEdit.setDate(QDate.fromString(doctor.get_request_time()))

        # Set the Patient's information
        patient = doctor.get_patient()
        self.ui.fullNameLineEdit.setText(patient.get_name())
        self.ui.dOBDateEdit.setDate(QDate.fromString(patient.get_dob()))
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

    def createDocument(self):
        doctor = parse(self.filePath)
        self.populate_information(doctor)






if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
