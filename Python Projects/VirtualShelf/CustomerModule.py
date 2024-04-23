class Customer:
    def __init__(self, name):
        # Initialize the customer with a name, a starting balance, and an empty list for purchased items.
        self.name = name
        self.balance = 15  # Assume starting balance is $15 for this customer.
        self.purchaseItems = []  # List to store purchased items.

    def __str__(self):
        # Return a string representation of the customer showing their name and current balance.
        return f"{self.name} ${self.balance:.2f}"
    
    def buy(self, item):
        # Allow the customer to buy an item if they have enough balance.
        if self.balance >= item._price:
            self.purchaseItems.append(item)  # Add the item to the purchase list.
            self.balance -= item._price  # Deduct  the item price from the balance.
            print(f"{item._title} added to cart. Remaining balance is ${self.balance:.2f}")
        else:
            # Inform the customer if they do not have enough balance to purchase the item.
            print(f"You don't have sufficient balance in your gift card. Current balance: ${self.balance:.2f}")

    def refund(self, id):
        # Process a refund by removing the item from the purchased list and refunding the price.
        for item in self.purchaseItems:
            if item._id == id:
                self.purchaseItems.remove(item)  # Remove the item from the list.
                self.balance += item._price  # Add the item price back to the balance.
                print(f"{item._title} removed from cart. Remaining balance is ${self.balance:.2f}")
                return
        # Notify if the item to refund is not found in the purchase list.
        print("The item you are trying to refund is not in your cart")

    def showItems(self):
        # Display all items the customer has purchased.
        print(f"{self.name}'s item list..............")
        for item in self.purchaseItems:
            print(item)
