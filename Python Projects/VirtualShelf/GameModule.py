from ItemModule import Item

class Game(Item):
    def __init__(self, id, title, price, publisher, isMultiplayer=False):
        # Initialize the Game instance by calling the __init__ method of the parent Item class.
        # The Game class extends Item with additional attributes for the publisher and multiplayer status.
        super().__init__(id, title, price)  # Call to the superclass (Item) constructor to set id, title, and price.
        self._publisher = publisher  # Set the publisher of the game.
        self._isMultiplayer = isMultiplayer  # Set the multiplayer status, defaults to False if not specified.

    def __str__(self):
        # Return a string representation of the game including its basic information from Item,
        # followed by publisher and multiplayer status.
        multiplayer_status = "Multiplayer" if self._isMultiplayer else "Not Multiplayer"
        # Combines the string representation of the base class with the game-specific details.
        return f"{super().__str__()} {self._publisher} {multiplayer_status}"
