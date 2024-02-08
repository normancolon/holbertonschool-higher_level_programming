#!/usr/bin/python3
"A module that defines a class named MyList that inherits from list."


class MyList(list):
    """A subclass of list that adds the ability to print the list in sorted order.
    
    Attributes:
        None
    """

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
