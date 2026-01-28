'''
Intro to OOP in Python, enhanced version
'''

class Grasshopper:
    '''
    A class representing a grasshopper.
    '''

    def __init__(self, name="", idade=0):
        '''
        Initialize the grasshopper with a name using the constructor method.
        '''
        self.name = name
        self.idade = idade

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

    def __str__(self):  # Dunder method for string representation
        '''
        Return a string representation of the grasshopper.
        '''
        return f"Grasshopper {self.name} is {self.idade} years old."
    
    def __getstate__(self):
        return self.__dict__

'''
Instance creation and method calls
'''
little_grasshopper = Grasshopper(name="Greenie", idade=2)      # Create an instance of Grasshopper

print(little_grasshopper.jump())        # Output: Greenie is jumping!
print(little_grasshopper.eat())         # Output: Greenie is eating!

print(little_grasshopper)               # Output: A class representing a grasshopper.

print(little_grasshopper.__getstate__())                        # Output: {'name': 'Greenie', 'idade': 2}