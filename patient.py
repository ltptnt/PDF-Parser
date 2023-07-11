from datetime import date

class patient:
    def __init__(self):
        self.name = None
        # dob is a datetime object
        self.dob = None
        self.address = None
        self.medicare = None
        self.age = None
        self.current_conditions = None
        self.phone_number = None
        self.date = None
    
    def set_name(self, name) -> None:
        self.name = name
    
    def set_dob(self, dob) -> None:
        self.dob = dob
        self.age = self.calculate_age(dob)
    
    def set_address(self, address) -> None:
        self.address = address
        
    def set_medicare(self, medicare) -> None:
        self.medicare = medicare
        
    def set_current_conditions(self, current_conditions) -> None:
        self.current_conditions = current_conditions
        
    def set_phone_number(self, phone_number) -> None:
        self.phone_number = phone_number
        
    def set_date(self, date) -> None:
        self.date = date
        
    def get_name(self) -> str | None:
        return self.name
    
    def get_dob(self) -> str | None:
        if self.dob is not None:
            return self.dob.strftime("%d/%m/%Y")
        return self.dob
    
    def get_address(self) -> str | None:
        return self.address
    
    def get_medicare(self) -> str | None:
        return self.medicare
    
    def get_age(self) -> int | None:
        return self.age
    
    def get_current_conditions(self) -> list | None:
        return self.current_conditions
    
    def get_phone_number(self) -> int | None:
        return self.phone_number
    
    def get_date(self) -> date | None:
        return self.date
    
    def __str__(self) -> str:
        return f"Name: {str(self.get_name())}\n \
                DOB: {str(self.get_dob())}\n \
                Address: {str(self.get_address())}\n \
                Medicare: {str(self.get_medicare())}\n \
                Age: {str(self.get_age())}\n \
                Current Conditions: {str(self.get_current_conditions())}\n \
                Phone Number: {str(self.get_phone_number())}\n \
                Date: {str(self.get_date())}\n"
    
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