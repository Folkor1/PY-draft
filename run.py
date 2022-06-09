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
    print("=" * 70)
    print("Hello and welcome to this very useful matrix determinant finder tool!")
    print("=" * 70)
    print("                               Enter the")
    print(colors.GREEN + "              __  __           _            _        ")
    print(colors.GREEN + "             |  \/  |   __ _  | |_   _ __  (_) __  __")
    print(colors.GREEN + "             | |\/| |  / _` | | __| | '__| | | \ \/ /")
    print(colors.GREEN + "             | |  | | | (_| | | |_  | |    | |  >  < ")
    print(colors.GREEN + "             |_|  |_|  \__,_|  \__| |_|    |_| /_/\_\ ")
    print(colors.WHITE + " ")
    print("=" * 70)
    print("")
    print("=" * 70)
    print(" ")
    print(" ")

def login_user():
    """
    Display the login message and validate the user input.
    """
    login_input = input('Type in the username: ')
    login = SHEET.worksheet('creds')
    login_col = login.col_values(1)
    pass_col = login.col_values(2)
    while True:
        try:
            if login_input not in login_col:
                print(f'No such user "{login_input}" exists. Please use the correct username.\n')
                login_user()
            else:
                print('Success!\n')
                login_ind = login_col.index(login_input)
            pass_input = input('Type in password: ')
            if pass_input not in pass_col:
                print('no pass succ1')
                login_user()
            else:
                pass_ind = pass_col.index(pass_input)
            if pass_ind != login_ind:
                print('no pass succ2')
            else:
                clear_console()
                print('Login successful!\n\n')
                how_to()
        except ValueError():
            print('error')

def clear_console():
    """
    Clear the console.
    """
    clear = os.system('clear')

def how_to():
    """
    Show 'How to' text.
    """
    print('==========================================================================================================')
    print('\nHow to:')
    print('\nEnter 2, 3 or 4 numbers, separated by comma.')
    print('\nDepending on which number you have entered, the programm will request next batch of numbers - 2, 3 or 4.')
    print('\nFor example, if you entered 3, then the program will request 3 more numbers 2 more times.')
    print('\nThen the program will return the matrix and its determinant.')
    print('\nExample:\n')
    print(colors.GREEN + '   3   4   5')
    print(colors.GREEN + '   0   8   1')
    print(colors.GREEN + '   9   7   6')
    print(colors.WHITE + '   \nThe matrix determinant is: -201')
    print('===========================================================================================================')

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



def main():
    welcome()
    login_user()

main()