'''
A class to represent a collaborator of a comphany
'''
class Collaborator:
    '''
    Creates the collaborator with basic attributes and methods
    '''
    def __init__(self, name, department, position, company = "CompCorp"):

        self.name = name
        self.department = department
        self.position = position
        self.company = company
    
    def PresentYourSelf(self):
    
        return print(f"Hi, my name is {self.name}. I'm the {self.position} at the {self.department} department at {self.company}")

c1 = Collaborator(name = "Maria", department = "Marketing", position = "Analyst")

c2 = Collaborator(name = "John", department = "IT", position = "Support Technician")

c1.PresentYourSelf()
c2.PresentYourSelf()
