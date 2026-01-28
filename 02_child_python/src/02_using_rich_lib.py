'''
This module demonstrates the use of the Rich library to create
a styled console output in Python.

rich library documentation: https://rich.readthedocs.io/en/stable/
'''

# Import necessary components from the Rich library
from rich.text import Text
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

texts = [
    "\nHello, Rich Library!",
    "\nWelcome to [blue]Python[/blue] programming!",
    "\n:earth_americas:"
    ]

def print_styled_texts():
    '''
    Print a list of styled text objects using Rich library.
    '''
    for text in texts:
        print(text)

def print_texts_in_styled_panel():
    '''
    Print a styled panel using Rich library.
    '''
    for text in texts:
        panel = Panel.fit(text, title=f"Rich Panel", border_style="green")
        print(panel)

def print_texts_in_styled_table():
    '''
    Print a styled table using Rich library.
    '''
    table = Table(title="Rich Text Table", show_header=True, header_style="bold magenta")
    table.add_column("Index", justify="center", style="white", width=6)
    table.add_column("Styled Text", justify='left', style="cyan")

    for index, text in enumerate(texts, start=1):
        table.add_row(str(index), text)

    console = Console()
    console.print(table)

if __name__ == "__main__":

    # Call the function to print styled texts
    print_styled_texts()
    print_texts_in_styled_panel()
    print_texts_in_styled_table()