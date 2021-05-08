class Employee: 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last, pay)
        if employees is None: 
            self.employees = []
        else: 
            self.employees = employees 
    
    def add_emp(self, emp):
        if emp not in self.employees: 
            self.employees.append(emp)


class Vessel:
    def __init__(self, imo_number, vessel_type, dwt, builder, equipment=[]):
        self.imo_number = imo_number
        self.vessel_type = vessel_type
        self.dwt = dwt
        self.builder = builder
        self.equipment = equipment 

    def add_equipment(self, bwts, scrubber):
        if bwts not in self.equipment:
            self.equipment.append(bwts)
        if scrubber not in self.equipment:
            self.equipment.append(scrubber)

class Tanker(Vessel):
    def __init__(self, imo_number, vessel_type, dwt, builder, equipment=[], tank_coating=None):
        super().__init__(self, imo_number, vessel_type, dwt, builder)
        self.equipment = equipment

        if tank_coating is None:
            self.tank_coating = []
        else:
            self.tank_coating = tank_coating
    
    def add_coating(self, coating):
        if coating not in self.tank_coating:
            self.tank_coating.aapend(coating)
        
green_attitude = Tanker(9876509, 'VLCC', 299999,'Hyundai Mipo', ['BWTS'])


print(green_attitude.equipment)

import numpy as np