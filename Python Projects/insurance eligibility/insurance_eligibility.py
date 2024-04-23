# This script calculates insurance premiums based on the user's age, speeding ticket history,
# and, for users under 25, whether they have passed a driving test. Eligible users are added
# to a list, and the premium amount is displayed.

eligibleName = []  # Initializes an empty list to store names of eligible users for insurance.

# Loop indefinitely to process multiple users until stopped by the user.
while True:
    name = str(input("Name: "))
    age = int(input("Age: "))
    ticketMessage = input('Have you received a speeding ticket anytime? Type Y (Yes) or N (No): ').upper()

    # Initialize variables to handle eligibility and premium amount.
    eligibleUser = False
    premiumAmmount = None

    # Checks conditions for users aged 25 or above.
    if age >= 25:
        if ticketMessage == "Y":
            premiumAmmount = 1000  # Premium amount for users with a ticket.
            eligibleUser = True
        elif ticketMessage == "N":
            premiumAmmount = 500   # Lower premium for users without a ticket.
            eligibleUser = True
        else:
            print('Wrong input.')

    # Check conditions for users below 25.
    elif age < 25:
        drivingTest = input('Have you taken a driving test? Type Y (Yes) or N (No): ').upper()
        if ticketMessage == "Y":
            if drivingTest == "Y":
                premiumAmmount = 1500  # Higher premium for young drivers with a ticket who passed the driving test.
                eligibleUser = True
            elif drivingTest == "N":
                eligibleUser = False  # Ineligible if failed the driving test and has a ticket.
            else:
                print('Wrong input.')
        
        elif ticketMessage == "N":
            if drivingTest == "Y":
                premiumAmmount = 1000  # Standard premium for young drivers without a ticket who passed the driving test.
                eligibleUser = True
            elif drivingTest == "N":
                premiumAmmount = 1500  # Penalty premium for young drivers without a ticket who failed the driving test.
                eligibleUser = True
            else:
                print('Wrong input.')
        else:
            print('Wrong input.')

    # Add eligible users to the list.
    if eligibleUser:
        eligibleName.append(name)

    # Display the premium amount or ineligibility message.
    if premiumAmmount is not None:
        print(f'Premium amount for the user would be: {premiumAmmount}')
        print('--------------------------------------------------------------------------------')
    else:
        print('User is ineligible for insurance.')
        print('--------------------------------------------------------------------------------')
    
    # Ask if the user wants to process another quote.
    finalQuestion = input('Do you want to get the quote for another person? Type Y (Yes) or N (No): ').upper()
    print('--------------------------------------------------------------------------------')
    if finalQuestion == "N":
        break
    elif finalQuestion == "Y":
        continue
    else:
        print('Wrong user input.')

# Display the list of eligible users.
print('The following is the list of eligible users:')
print(eligibleName)
