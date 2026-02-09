# Import necessary components from the Rich library
'''
 To list all the availabe emojis for rich library, run the following command in terminal:
 
 python -m rich.emoji
'''
from rich.text import Text
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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
    
        return print(f":handshake: Hi, my name is [blue]{self.name}[/blue]. I'm the {self.position} at the {self.department} department at {self.company}")

c1 = Collaborator(name = "Maria", department = "Marketing", position = "Analyst")

c2 = Collaborator(name = "John", department = "IT", position = "Support Technician")

c1.PresentYourSelf()
c2.PresentYourSelf()
