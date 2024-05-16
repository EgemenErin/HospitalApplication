import pickle
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, surname, pesel, username, password):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.username = username
        self.password = password

    def get_details(self):
        pass