from datetime import timedelta
from employee import Employee
from oncallduty import OnCallDuty

class Nurse(Employee):
    def __init__(self, name, surname, pesel, username, password):
        super().__init__(name, surname, pesel, username, password)
        self.on_call_duties = []

    def add_on_call_duty(self, duty_date):
        if len(self.on_call_duties) >= 10:
            raise ValueError("Maximum number of on-call duties reached.")
        if self.on_call_duties and any(duty_date == d.duty_date + timedelta(days=1) for d in self.on_call_duties):
            raise ValueError("Cannot schedule on consecutive days.")
        self.on_call_duties.append(OnCallDuty(self, duty_date))

    def get_details(self):
        return f"Nurse {self.name} {self.surname}"
