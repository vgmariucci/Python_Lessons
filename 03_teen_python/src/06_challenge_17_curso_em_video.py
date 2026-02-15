'''
 To list all the availabe emojis for rich library, run the following command in terminal:
 
 python -m rich.emoji
'''
# Import necessary components from the Rich library
from rich.text import Text
from rich import print
from rich.console import Console
from rich.panel import Panel


class ProductTag:
    '''
    A class to represent a product tag
    '''
    def __init__(self, product_name, price):
        
        self.name = product_name
        self.price = price
    
    def print_product_tag(self):
        return print(
                    Panel(
                          Text(f"{self.name}\n----------\nR${self.price:,.2f}",justify = "center"), 
                        title_align = "center",
                        title = "Product"
                        )
                    )
    


p1 = ProductTag(product_name = "Pen", price = 3.5)
p1.print_product_tag()

