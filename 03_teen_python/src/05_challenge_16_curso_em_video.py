'''
A class to represent a colaborator of a comphany
'''
class Colaborator:
    '''
    Creates the colaborator with basic attributes and methods
    '''
    def __init__(self, name, department, position, company = "CompCorp"):

        self.name = name
        self.department = department
        self.position = position
        self.company = company
    
    def PresentYourSelf(self):
    
        return print(f"Hi, my name is {self.name}. I'm the {self.position} at the {self.department} department at {self.company}")

c1 = Colaborator(name = "Maria", department = "Marketing", position = "Analyst")

c2 = Colaborator(name = "John", department = "IT", position = "Support Technician")

c1.PresentYourSelf()
c2.PresentYourSelf()
