from ItemModule import Item

class Movie(Item):
    def __init__(self, id, title, price, runningTime):
        # Initialize the Movie instance using the Item class constructor to set common attributes.
        # Additionally, set the runningTime which is specific to Movie objects.
        super().__init__(id, title, price)  # Calls the constructor of the parent class (Item).
        self._runningTime = runningTime  # Private attribute to store the running time of the movie.

    def __str__(self):
        # Overridden method to return a string representation of the Movie.
        # This includes the ID, price, title from the Item class plus the running time specific to the Movie.
        # Format: ID $ Price Title RunningTime
        return f"{super().__str__()} {self._runningTime} minutes"
