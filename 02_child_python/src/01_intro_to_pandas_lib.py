'''
Importing the pandas library and checking its version.
'''
import pandas as pd


def hello_pandas():
    '''
    A simple function to demonstrate pandas functionality.
    '''
    print(f"Pandas version: {pd.__version__}")
    # Sample code to create a simple DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)

# Call the function to demonstrate pandas usage
if __name__ == "__main__":
    hello_pandas()