import gspread
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Enter_the_Matrix')

class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'

def welcome():
    """
    Welcome message.
    """
    print("======================================================================")
    print("Hello and welcome to this very useful matrix determinant finder tool!")
    print("======================================================================")
    print(" ")
    print("                               Enter the")
    print(colors.GREEN + "              __  __           _            _        ")
    print(colors.GREEN + "             |  \/  |   __ _  | |_   _ __  (_) __  __")
    print(colors.GREEN + "             | |\/| |  / _` | | __| | '__| | | \ \/ /")
    print(colors.GREEN + "             | |  | | | (_| | | |_  | |    | |  >  < ")
    print(colors.GREEN + "             |_|  |_|  \__,_|  \__| |_|    |_| /_/\_\ ")
    print(colors.WHITE + " ")
    print("======================================================================")
    print("")
    print("======================================================================")
    print(" ")
    print(" ")

def start_menu():
    """ 
    Select between 2 options,
    view instructions or login.
    """
    print('Please select one the the following options:\n')
    print('1 - Show "How to"')
    print('2 - Login')
    main_input()

def main_input():
    """
    Validate the input on main screen.
    """
    first_input = input()
    while True:     
        if first_input == "1":
            clear_console()
            how_to()
        elif first_input == "2":
            clear_console()
            login_user()
        else:
            print(f"\nYou entered: {first_input}. Please enter 1 or 2.")
            main_input()
        return

def clear_console():
    """
    Clear the console.
    """
    clear = os.system('clear')

def how_to():
    """
    Show 'How to' text.
    """
    print('\nEnter 2, 3 or 4 numbers, separated by comma.')
    print('\nDepending on which number you have entered, the programm will request next batch of numbers - 2, 3 or 4.')
    print('\nFor example, if you entered 3, then the program will request 3 more numbers 2 more times.')
    print('\nThen the program will return the matrix and its determinant.')
    print('\nExample:\n')
    print(colors.GREEN + '   3   4   5')
    print(colors.GREEN + '   0   8   1')
    print(colors.GREEN + '   9   7   6')
    print(colors.WHITE + '   \nThe matrix determinant is: -201')
    how_to_continue()

def how_to_continue():
    """
    Select between 2 options: log in or return to the start screen.
    """
    print('\n\nPlease select one the the following options:\n')
    print('1 - Return to the start screen')
    print('2 - Login')
    how_to_validate()

def how_to_validate():
    """
    Validate the input on 'How to' screen.
    """
    how_to_input = input()
    while True:
        if how_to_input == "1":
            clear_console()
            welcome()
            start_menu()
        elif how_to_input == "2":
            clear_console()
            login_user()
        else:
            print(f"\nYou entered: {how_to_input}. Please enter 1 or 2.")
            how_to_validate()
        return

def login_user():
    """
    Display the login message and validate the user input.
    """
    login_input = input('Enter the username: ')
    login = SHEET.worksheet('creds')
    login_col = login.col_values(1)
    while True:
        try:
            if login_input not in login.col_values(1):
                print('No such a user exists. Please enter the correct username.\n')
                login_user()
            else:
                print('succ')
            return
        except ValueError():
            print('error')

def main():
    welcome()
    start_menu()

main()