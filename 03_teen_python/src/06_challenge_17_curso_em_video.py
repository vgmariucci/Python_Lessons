# Import necessary components from the Rich library
from rich.text import Text
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

class ProductTag:
    '''
    A class to represent a price tag for products
    '''
    def __init__(self, product_name, price):
        
        self.name = product_name
        self.price = price
    
    def print_product_tag(self):
        return print(f"Product name: {self.name}\nPrice: R$ {self.price:,.2f}")
    


p1 = ProductTag(product_name = "Pen", price = 3.5)
p1.print_product_tag()