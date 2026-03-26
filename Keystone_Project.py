import csv
import datetime

def load_data():
    users = {} 
    # TODO: Open 'database.txt' in read mode.
    # TODO: Use csv.reader to loop through the rows.
    # TODO: Store data in the 'users' dictionary. 
    # Use the PIN (row 1) as the Key, and [Name, Balance] as the Value.
    return users

def save_data(users):
    # TODO: Open 'database.txt' in 'w' (write) mode.
    # TODO: Use csv.writer to loop through the 'users' dictionary.
    # TODO: Write each user back to the file in the format: Name, PIN, Balance.
    pass

def main():
    print("=== PROJECT: SECURE ATM SYSTEM ===")
    data = load_data()
    
    pin = input("Please enter your PIN: ")
    
    # TODO: Check if the entered PIN exists in our 'data' dictionary.
    if False: # Replace 'False' with your dictionary check
        print("Access Granted.")
        
        # TODO: Get the user's name and balance from the dictionary.
        
        try:
            amount = int(input("Withdrawal amount: $"))
            # TODO: Check if they have enough money.
            # TODO: Update the balance in the dictionary.
            # TODO: Call save_data() to update the text file.
            
            # TODO: Use the 'datetime' library to print a timestamped receipt.
            
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid PIN.")

if __name__ == "__main__":
    main()
