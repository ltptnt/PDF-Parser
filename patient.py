from datetime import date

class Patient:
    def __init__(self):
        self.full_name = None
        # dob is a datetime object
        self.dob = None
        self.home_address = None
        self.medi_number = None
        self.age = None
        self.current_conditions = None
        self.medications = None
        self.phone_number = None
        self.dob_age = None
        self.community_pharmacist = None
        self.height = None
        self.weight = None
        self.blood_pressure = None
        self.creatine = None
        self.CrCl = None
        self.request_time = None
        self.accredited_pharmacist = None
    
    def set_name(self, name) -> None:
        self.full_name = name
    
    def set_dob(self, dob) -> None:
        self.dob = dob.strftime("%d/%m/%Y")
        self.age = self.calculate_age(dob)
        self.dob_age = f"{self.dob} ({self.age}yrs old)"
    
    def set_address(self, address) -> None:
        self.home_address = address
        
    def set_medicare(self, medicare) -> None:
        self.medi_number = medicare
        
    def set_current_conditions(self, current_conditions : list) -> None:
        self.current_conditions = current_conditions
        
    def set_phone_number(self, phone_number) -> None:
        self.phone_number = phone_number
        
    def set_date(self, date) -> None:
        self.request_time = date
    
    def set_height(self, height) -> None:
        self.height = height

    def set_weight(self, weight) -> None:
        self.weight = weight

    def set_blood_pressure(self, blood_pressure) -> None:
        self.blood_pressure = blood_pressure

    def set_creatine(self, creatine) -> None:
        self.creatine = creatine

    def set_CrCl(self, CrCl) -> None:
        self.CrCl = CrCl

    def set_accredited_pharmacist(self, accredited_pharmacist) -> None:
        self.accredited_pharmacist = accredited_pharmacist

    def set_medications(self, medications) -> None:
        self.medications = medications

    def get_medications(self) -> dict | None:
        return self.medications
    

    def get_height(self) -> str | None:
        return self.height
    
    def get_weight(self) -> str | None:
        return self.weight
    
    def get_blood_pressure(self) -> str | None:
        return self.blood_pressure
    
    def get_creatine(self) -> str | None:
        return self.creatine
    
    def get_CrCl(self) -> str | None:
        return self.CrCl
        
    def get_name(self) -> str | None:
        return self.full_name
    
    def get_dob(self) -> str | None:
        return self.dob
    
    def get_address(self) -> str | None:
        return self.home_address
    
    def get_medicare(self) -> str | None:
        return self.medi_number
    
    def get_age(self) -> str | None:
        return self.age
    
    def get_current_conditions(self) -> list | str | None:
        return self.current_conditions
    
    def get_phone_number(self) -> str | None:
        return self.phone_number
    
    def get_date(self) -> date | None:
        return self.request_time
    
    def get_dob_age(self) -> str | None:
        return self.dob_age
    
    def get_community_pharmacist(self) -> str | None:
        return self.community_pharmacist
    
    def set_community_pharmacist(self, community_pharmacist) -> None:
        self.community_pharmacist = community_pharmacist
    
    def get_accredited_pharmacist(self) -> str | None:
        return self.accredited_pharmacist
    
    @staticmethod    
    def calculate_age(dob):
        today = date.today()
        if today.month < dob.month:
            age = today.year - dob.year - 1
        elif today.month == dob.month and today.day < dob.day:
            age = today.year - dob.year - 1
        else:
            age = today.year - dob.year
        return age