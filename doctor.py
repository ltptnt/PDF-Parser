import patient
class doctor:
    def __init__(self) -> None:
        self.name = None
        self.nurse_name = None
        self.community_pharmacy = None
        self.prescriber_number = None
        self.provider_number = None
        self.contact_number = None
        self.fax_number = None
        self.address = None
        self.email = None
        self.patient = patient.patient()
    
    def set_name(self, name) -> None:
        self.name = name
        
    def set_nurse_name(self, nurse_name) -> None:
        self.nurse_name = nurse_name
        
    def set_community_pharmacy(self, community_pharmacy) -> None:
        self.community_pharmacy = community_pharmacy
        
    def set_prescriber_number(self, prescriber_number) -> None:
        self.prescriber_number = prescriber_number
    
    def set_provider_number(self, provider_number) -> None:
        self.provider_number = provider_number
        
    def set_contact_number(self, contact_number) -> None:
        self.contact_number = contact_number
        
    def set_fax_number(self, fax_number) -> None:
        self.fax_number = fax_number
    
    def set_address(self, address) -> None:
        self.address = address
        
    def set_email(self, email) -> None:
        self.email = email
    
    def set_patient(self, patient) -> None:
        self.patient = patient
            
    def get_name(self) -> str | None:
        return self.name
    
    def get_nurse_name(self) -> str | None:
        return self.nurse_name
    
    def get_community_pharmacy(self) -> str | None:
        return self.community_pharmacy
    
    def get_prescriber_number(self) -> str | None:
        return self.prescriber_number
    
    def get_provider_number(self) -> str | None:
        return self.provider_number
    
    def get_contact_number(self) -> str | None:
        return self.contact_number
    
    def get_fax_number(self) -> str | None:
        return self.fax_number
    
    def get_address(self) -> str | None:
        return self.address
    
    def get_email(self) -> str | None:
        return self.email
    
    def get_patient(self) -> patient.patient | None:
        return self.patient
    
    def __str__(self) -> str:
        return f"Name: {self.name}\n \
                 Nurse Name: {self.nurse_name}\n \
                 Community Pharmacy: {self.community_pharmacy}\n \
                 Prescriber Number: {self.prescriber_number}\n \
                 Provider Number: {self.provider_number}\n \
                 Contact Number: {self.contact_number}\n \
                 Fax Number: {self.fax_number}\n \
                 Address: {self.address}\n \
                 Email: {self.email}\n \
                 Patient: {str(self.patient)}"
