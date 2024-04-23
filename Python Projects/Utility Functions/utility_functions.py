def pangram(string):
    # Check if the input string is a pangram, which contains every letter of the alphabet at least once.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

def even_indices(lst):
    # Return the indices of even numbers in the list.
    even_positions = []
    for i, num in enumerate(lst):
        if num % 2 == 0:
            even_positions.append(i)
    return even_positions

def encrypt(string):
    # Encrypt the string by shifting each character to the next character in the ASCII table.
    encrypted = ""
    for char in string:
        encrypted += chr(ord(char) + 1)
    return encrypted

def intersection(lst1, lst2):
    # Return a list containing the common elements of lst1 and lst2.
    return [x for x in lst1 if x in lst2]

def main():
    # Main menu function to allow the user to choose an action.
    while True:
        print("Menu:")
        print("1 : Check Pangram String")
        print("2 : List of positions of even numbers")
        print("3 : Encrypt the String")
        print("4 : Intersection of lists")
        print("0 : Exit")
        choice = int(input("Enter your choice (0-4): "))

        if choice == 1:
            string = input("Enter a string: ")
            result = pangram(string)
            if result:
                print("The string is a pangram.")
            else:
                print("The string is not a pangram.")

        elif choice == 2:
            lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
            result = even_indices(lst)
            print("The positions of even numbers are:", result)

        elif choice == 3:
            string = input("Enter a string: ")
            result = encrypt(string)
            print("The encrypted string is:", result)

        elif choice == 4:
            lst1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
            lst2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
            result = intersection(lst1, lst2)
            print("The intersection of the lists is:", result)

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
