from Patient import Patient
class Doctor:
    def __init__(self) -> None:
        self.full_name = None
        self.prescriber_number = None
        self.provider_num = None
        self.contact_number = None
        self.address = None
        self.email = None
        self.pref_contact = None
        self.request_time = None
        self.reason_for_referral = None
        self.patient = Patient()
    
    def set_name(self, name) -> None:
        self.name = name

    def set_community_pharmacy(self, community_pharmacy) -> None:
        self.community_pharmacist = community_pharmacy
        
    def set_prescriber_number(self, prescriber_number) -> None:
        self.prescriber_number = prescriber_number
    
    def set_provider_number(self, provider_number) -> None:
        self.provider_num = provider_number
        
    def set_contact_number(self, contact_number) -> None:
        self.contact_number = contact_number
        self.set_pref_contact()

    def set_address(self, address) -> None:
        self.address = address
        
    def set_email(self, email) -> None:
        self.email = email
        self.set_pref_contact()
    
    def set_request_time(self, request_time) -> None:
        self.request_time = request_time

    def set_reason_for_referral(self, reason_for_referral) -> None:
        self.reason_for_referral = reason_for_referral

    def set_pref_contact(self) -> None:
        if self.contact_number is not None and self.email is not None:
            self.pref_contact = f"Phone: {self.contact_number} or Email: {self.email}"
        elif self.contact_number is not None:
            self.pref_contact = self.contact_number
        elif self.email is not None:
            self.pref_contact = self.email

    def set_patient(self, patient) -> None:
        self.patient = patient
            
    def get_name(self) -> str | None:
        return self.name
        
    def get_community_pharmacist(self) -> str | None:
        return self.community_pharmacist
    
    def get_prescriber_number(self) -> str | None:
        return self.prescriber_number
    
    def get_provider_number(self) -> str | None:
        return self.provider_num
    
    def get_contact_number(self) -> str | None:
        return self.contact_number
    
    def get_address(self) -> str | None:
        return self.address
    
    def get_email(self) -> str | None:
        return self.email
    
    def get_patient(self) -> Patient | None:
        return self.patient
    
    def get_pref_contact(self) -> str | None:
        # Return a string of the phone number and email address
        return f"Phone: {self.contact_number} or Email: {self.email}"

    def get_request_time(self) -> str | None:
        return self.request_time
    
    def get_reason_for_referral(self) -> str | None:
        return self.reason_for_referral
    