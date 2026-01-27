'''
This module demonstrates the use of the Rich library to create
a styled console output in Python.

rich library documentation: https://rich.readthedocs.io/en/stable/
'''

# Import necessary components from the Rich library
from rich.text import Text
from rich import print
from rich.console import Console


if __name__ == "__main__":
    # Create a console object for rich text output
    console = Console()
    # Create a styled text object
    styled_texts_list = [
        "\nHello, Rich Library!",
        "\nWelcome to [blue]Python[/blue] programming!",
        "\n:earth_americas:"
    ]

    # Print the styled text to the console
    for styled_text in styled_texts_list:
        print(styled_text)