'''
Intro to OOP in Python
'''

class Grasshopper:
    '''
    A class representing a grasshopper.
    '''

    def __init__(self):
        '''
        Initialize the grasshopper with a name.
        '''
        self.name = ""

    def jump(self):
        '''
        Make the grasshopper jump.
        '''
        return f"{self.name} is jumping!"
    
    def eat(self):
        '''
        Make the grasshopper eat.
        '''
        return f"{self.name} is eating!"


little_grasshopper = Grasshopper()      # Create an instance of Grasshopper
little_grasshopper.name = "Greenie"     # Set the name attribute

print(little_grasshopper.jump())        # Output: Greenie is jumping!
print(little_grasshopper.eat())         # Output: Greenie is eating!