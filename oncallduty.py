from datetime import date,timedelta
class OnCallDuty:
    def __init__(self,person,duty_date):
        self.person = person
        self.duty_date = duty_date

    def __repr__(self):
        return f"{self.duty_date}: {self.person.name} {self.person.surname}"