class Item:
    def __init__(self, id, title, price):
        # Constructor for the Item class. Initializes an item with an ID, title, and price.
        self._id = id  # Private variable to store the unique identifier of the item.
        self._title = title  # Private variable to store the title of the item.
        self._price = price  # Private variable to store the price of the item.

    def __str__(self):
        # Overridden method to return a string representation of the item.
        # This is useful for displaying item information in a user-friendly format.
        # Returns the ID, price, and title of the item formatted as a string.
        return f"{self._id} $ {self._price:.2f} {self._title}"
