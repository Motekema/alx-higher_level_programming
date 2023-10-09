#!/usr/bin/python3
"""
Module: my_list

"""

class MyList(list):
    """
    MyList class, inherits from list.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list sorted in ascending order.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))

