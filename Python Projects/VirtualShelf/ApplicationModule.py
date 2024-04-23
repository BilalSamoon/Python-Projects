# This module defines the Application class to handle the business logic of a media store app.

from GameModule import Game
from MovieModule import Movie
from CustomerModule import Customer

class Application:
    def __init__(self):
        # Initialize the Application with a dictionary of items for sale and a default customer.
        self.itemDictionary = {
            "M101": Movie(id="M101", title="Spongebob", price=4.99, runningTime=98),
            "M102": Movie(id="M102", title="Tom and Jerry", price=6.99, runningTime=102),
            "G101": Game("G101", "Minecraft", 3.99, "Energetic Inc", True),
            "G102": Game("G102", "Mario", 7.99, "Super Inc", False)
        }
        self.jack = Customer("Jack")

    def run(self):
        # Start the application, display items, handle purchases and returns.
        print(self.jack)

        # Offer items for sale to the customer.
        while True:
            for item in self.itemDictionary.values():
                print(item)
            item_id = input("Please enter the item id to purchase (enter 'none' to stop): ")
            if item_id.lower() == 'none':
                break
            if item_id in self.itemDictionary:
                self.jack.buy(self.itemDictionary[item_id])
            else:
                print("The id you entered is not available at the store")

        # Display purchased items.
        self.jack.showItems()

        # Allow customer to return items.
        while True:
            for item in self.jack.purchaseItems:
                print(item)
            item_id = input("Please enter the item id to remove (enter 'none' to stop): ")
            if item_id.lower() == 'none':
                break
            self.jack.refund(item_id)

        # Final display of items post return process.
        self.jack.showItems()

# Startup code to run the application.
if __name__ == "__main__":
    app = Application()
    app.run()
