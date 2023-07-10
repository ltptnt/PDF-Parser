from datetime import date

class patient:
    def __init__(self, name, dob, address, medicare):
        self.name = name
        # dob is a datetime object
        self.dob = dob
        self.address = address
        self.medicare = medicare
        # calculate age
        self.age = self.calculate_age(dob)
    
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