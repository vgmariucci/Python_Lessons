'''
This script deals with some math operations with Python and object oriented programming (OOP).
'''

class MathOperations:
    @staticmethod
    def add(a, b):
        """
        Returns the sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Returns the difference of a and b.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Returns the product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Returns the quotient of a divided by b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def module(a, b):
        """
        Returns the modulo of a by b.
        """
        return a % b
    

if __name__ == "__main__":
    
    a = [1431655764, 1431655765, 1431655766]
    b = 3
    
    math_ops = MathOperations()

    print("="*20)
    print(f"Math operations with elements {a} and {b}")
    print("="*20)
    
    for element in a:
        
        print("-"*20)

        print(f"Addition of {element} + {b}: {math_ops.add(element,b)}")
        
        print(f"Subtraction of {element} - {b}: {math_ops.subtract(element,b)}")
       
        print(f"Multiplication of {element} . {b}: {math_ops.multiply(element,b)}")
        
        print(f"Division of {element} / {b}: {math_ops.divide(element,b)}")
              
        print(f"Module of {element} % {b}: {math_ops.module(element,b)}")
        
        print("-"*20)