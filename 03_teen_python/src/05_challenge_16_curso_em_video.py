# Import necessary components from the Rich library
'''
 To list all the availabe emojis for rich library, run the following command in terminal:
 
 python -m rich.emoji
'''
from rich.text import Text
from rich import print
from rich import inspect

class Collaborator:
    '''
    Creates the collaborator with basic attributes and methods
    '''
    # Class attributes
    company = "CompCorp"

    def __init__(self, name, department, position):
        # Instance attributes
        self.name = name
        self.department = department
        self.position = position
    
    def PresentYourSelf(self):
    
        return f":handshake: Hi, my name is [blue]{self.name}[/blue]. I'm the {self.position} at the {self.department} department at {Collaborator.company}"

c1 = Collaborator(name = "Maria", department = "Marketing", position = "Analyst")

c2 = Collaborator(name = "John", department = "IT", position = "Support Technician")

print(c1.PresentYourSelf())
print(c2.PresentYourSelf())

# inspect(c1, methods = True)