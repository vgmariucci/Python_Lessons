'''
This Python script is intended to implement the FizzBuzz problem.
The FizzBuzz problem is a common programming challenge where you print numbers from 1 to 100.
'''

def FizzBuzz():
    '''
    - For multiples of three, print "Fizz" instead of the number.
    - For multiples of five, print "Buzz" instead of the number.
    - For numbers which are multiples of both three and five, print "FizzBuzz".
    '''
    for i in range(1,100):
        
        if(i % 3 == 0 and not(i % 5 == 0)):
            print(f"{i} Fizz")

        if(i % 5 == 0 and not(i % 3 == 0)):
            print(f"{i} Buzz")

        if(i % 15 == 0):
            print(f"{i} FizzBuzz")
        
        else:
            print(i)
    
# Call the FizzBuzz function to execute the logic
if __name__ == "__main__":
    FizzBuzz()
