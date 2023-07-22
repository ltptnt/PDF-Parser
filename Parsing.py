import pdfplumber
from datetime import date
from Doctor import Doctor
from Patient import Patient

# Read in the two example files
def parse(file_path : str)-> Doctor:
  pdf = pdfplumber.open(file_path)
  doctor = template_1(pdf)
  if doctor.get_reason_for_referral() is None:
      doctor.set_reason_for_referral("Polypharmacy")
  return doctor


def template_1(pdf):
    # For the first template, we'll extract the text from the first page
    # and then split it into lines
    page = pdf.pages[0]
    text = page.extract_text()
    lines = text.split("\n")

    new_doctor = Doctor()
    new_patient = Patient()
    pharmacist_name = None

    for line in lines:
        # Get doctor name, patient name
        if "Name:" in line and new_doctor.get_name() is None:
            new_doctor.set_name(line.split("Name:")[1].strip())
            continue
        elif "Name:" in line and new_patient.get_accredited_pharmacist() is None:
            pharmacist_name = line.split("Name:")[1].strip()
            new_patient.set_accredited_pharmacist(pharmacist_name)
            continue

        elif "Name:" in line and new_patient.get_name() is None:
            new_patient.set_name(line.split("Name:")[1].strip())
            continue
        
        # Get patient phone number, doctor phone number
        if "Phone:" in line and new_doctor.get_contact_number() is None:
            new_doctor.set_contact_number(line.split("Phone:")[1].strip())
            continue
        elif "Phone:" in line and new_patient.get_phone_number is None:
            new_patient.set_phone_number(line.split("Phone:")[1].strip())
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

        if "Medicare No:" in line and new_patient.get_medicare() is None:
            new_patient.set_medicare(line.split("Medicare No:")[1].strip())
            continue    
        
        if "Community Pharmacy:" in line and new_patient.get_community_pharmacist() is None:
            new_patient.set_community_pharmacist(line.split("Community Pharmacy:")[1].strip())
            continue
        
        # Get doctor details
        if "Provider No:" in line and new_doctor.get_provider_number() is None:
            new_doctor.set_provider_number(line.split("Provider No:")[1].strip())
            continue
        
        if "Prescriber No:" in line and new_doctor.get_prescriber_number() is None:
            new_doctor.set_prescriber_number(line.split("Prescriber No:")[1].strip())    
            continue
                
        if "Email:" in line and new_doctor.get_email() is None:
            new_doctor.set_email(line.split("Email:")[1].strip())
            continue

        
    # Get the date an Currrent Conditions from the second page
    page = pdf.pages[1]
    text = page.extract_text()
    lines = text.split("\n")

    for line in lines:
        if "Date:" in line and new_patient.get_date() is None:
            new_patient.set_date(line.split(" ")[1].strip())
            continue
        if "Height:" in line and new_patient.get_height() is None:
            new_patient.set_height(line.split(" ")[1].strip())
            continue
        if "Weight:" in line and new_patient.get_weight() is None:
            new_patient.set_weight(line.split(" ")[1].strip())
            continue


    current_conditions = text.split("CURRENT CONDITIONS:")[1]
    current_conditions = current_conditions.split("RELEVANT LABORATORY RESULTS AND BLOOD DRUG LEVELS (eg serum electrolytes, liver function test etc. as relevant)")[0]
    current_conditions = current_conditions.split("\n")

    conditions = []
    for condition in current_conditions:
        if condition != "":
            conditions.append(condition.strip())

    new_patient.set_current_conditions(conditions)


    # Get the medications from the 2nd page
    # Crop the page to only include the left side of the page
    page = pdf.pages[1]
    # change the margin to be 0
    page = page.within_bbox((0, 0, page.width, page.height))
    left_side = page.crop((0, 0, page.width / 2, page.height))
    right_side = page.crop((page.width / 2, 0, page.width, page.height))
    table_strat = {"vertical_strategy": "text", "horizontal_strategy": "text", "text_x_tolerance": 1, "text_y_tolerance": 1}
    l_tables = left_side.extract_table(table_settings=table_strat)
    r_text = right_side.extract_text()
    dosages = r_text.split("\n")

    medications = []
    for table in l_tables:
        medication = ''.join(table)
        medications.append(medication)
    # Split the list to only the first part of the list excluding the title which is the medications
    medications = medications[4:medications.index("CURRENT CONDITIONS:") - 1]
    
    dosages = dosages[0:dosages.index('S (eg serum electrolytes, liver function test etc. as relevant)')]
    
    # covert the dosages to a dictionary. If thee is a medication with no value then the values for the next two medications will be the value for the previous medication
    medication_dict = {}
    multi_line_adjustment = 0
    for i in range(len(medications)):
        if medications[i] == "":
            multi_line_medication = dosages[i - 1] + dosages[i] + dosages[i + 1] + dosages[i + 2]
            multi_line_adjustment += 2
            medication_dict[medications[i - 1]] = multi_line_medication
        else:
            medication_dict[medications[i]] = dosages[i + multi_line_adjustment]
    
    # Add the medications to the patient
    new_patient.set_medications(medication_dict)
        


    # Set the doctor and patient
    new_doctor.set_patient(new_patient)
    return new_doctor

parse("example1.pdf")