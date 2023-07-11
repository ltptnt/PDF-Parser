import pdfplumber
from datetime import date
import doctor
import patient

# Read in the two example files
pdf1 = pdfplumber.open("example1.pdf")
pdf2 = pdfplumber.open("example2.pdf")



def template_1(pdf):
    # For the first template, we'll extract the text from the first page
    # and then split it into lines
    page = pdf1.pages[0]
    text = page.extract_text()
    lines = text.split("\n")
    print(lines)

    new_doctor = doctor.doctor()
    new_patient = patient.patient()

    for line in lines:
        # Get Pharmcist name, doctor name, patient name
        if "Name:" in line and new_doctor.get_name() is None:
            new_doctor.set_name(line.split("Name:")[1].strip())
            continue
        elif "Name:" in line and new_doctor.get_nurse_name() is None:
            new_doctor.set_nurse_name(line.split("Name:")[1].strip())
            continue
        elif "Name:" in line and new_patient.get_name() is None:
            new_patient.set_name(line.split("Name:")[1].strip())
            continue
        

        # Get Doctor address, patient address
        if "Address:" in line and new_doctor.get_address() is None:
            new_doctor.set_address(line.split("Address:")[1].strip())
            continue
        elif "Address:" in line and new_patient.get_address() is None:
            new_patient.set_address(line.split("Address:")[1].strip())
            continue
        
        # Get patient details
        if "D.O.B:" in line and new_patient.get_dob() is None:
            DOB = line.split("D.O.B:")[1].strip()
            # Convert DOB to datetime object
            date_of_birth = date(int(DOB.split("/")[2]), int(DOB.split("/")[1]), int(DOB.split("/")[0]))
            new_patient.set_dob(date_of_birth)
        
        #
        if "Medicare No:" in line and new_patient.get_medicare() is None:
            new_patient.set_medicare(line.split("Medicare No:")[1].strip())
            continue    
        
        if "Community Pharmacy:" in line and new_doctor.get_community_pharmacy() is None:
            new_doctor.set_community_pharmacy(line.split("Community Pharmacy:")[1].strip())
            continue
        
        if "Provider No:" in line and new_doctor.get_provider_number() is None:
            new_doctor.set_provider_number(line.split("Provider No:")[1].strip())
            continue
        
        if "Prescriber No:" in line and new_doctor.get_prescriber_number() is None:
            new_doctor.set_prescriber_number(line.split("Prescriber No:")[1].strip())    
            continue
        
        if "Phone:" in line and new_doctor.get_contact_number() is None:
            new_doctor.set_contact_number(line.split("Phone:")[1].strip())
            continue
        elif "Phone:" in line and new_patient.get_phone_number is None:
            new_patient.set_phone_number(line.split("Phone:")[1].strip())
            continue
            
        if "Fax:" in line and new_doctor.get_fax_number() is None:
            new_doctor.set_fax_number(line.split("Fax:")[1].strip())
            continue
        
        if "Email:" in line and new_doctor.get_email() is None:
            new_doctor.set_email(line.split("Email:")[1].strip())
            continue
        
        

    # Get the date an Currrent Conditions from the second page
    page = pdf1.pages[1]
    text = page.extract_text()
    lines = text.split("\n")

    current_conditions = text.split("CURRENT CONDITIONS:")[1]
    current_conditions = current_conditions.split("RELEVANT LABORATORY RESULTS AND BLOOD DRUG LEVELS (eg serum electrolytes, liver function test etc. as relevant)")[0]
    current_conditions = current_conditions.split("\n")

    conditions = []
    for condition in current_conditions:
        if condition != "":
            conditions.append(condition.strip())

    new_patient.set_current_conditions(conditions)

    for line in lines:
        if "Date:" in line and new_patient.get_date() is None:
            new_patient.set_date(line.split(" ")[1].strip())
            continue

    # Set the doctor and patient
    new_doctor.set_patient(new_patient)
    return new_doctor

doctor1 = template_1(pdf1)
print(doctor1.get_name())