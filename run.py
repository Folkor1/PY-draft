import gspread
import os
import numpy as np
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
    WHITE = '\033[97m'

class Matrix:
    def __init__(self, row):
        self.row = row

    def built_matrix(self):
        return f"{self.row}"

def welcome():
    """
    Welcome message.
    """
    print("\n\n")
    print("=" * 70)
    print("Hello and welcome to this very useful matrix determinant finder tool!")
    print("=" * 70)
    print("\n                               Enter the")
    print(colors.GREEN + "              __  __           _            _        ")
    print(colors.GREEN + "             |  \/  |   __ _  | |_   _ __  (_) __  __")
    print(colors.GREEN + "             | |\/| |  / _` | | __| | '__| | | \ \/ /")
    print(colors.GREEN + "             | |  | | | (_| | | |_  | |    | |  >  < ")
    print(colors.GREEN + "             |_|  |_|  \__,_|  \__| |_|    |_| /_/\_\ ")
    print(colors.WHITE + " ")
    print("=" * 70)
    print("")
    print("=" * 70)
    login_user()

def login_user():
    """
    Display the login message and validate the user/password input.
    """
    login_input = input('\nType in the username: ')
    login = SHEET.worksheet('creds')
    login_col = login.col_values(1)
    pass_col = login.col_values(2)
    while True:
        try:
            if login_input not in login_col:
                print(f'No such user "{login_input}" exists. Please use the correct username.\n')
                login_user()
            else:
                print('Username correct.\n')
                pass_input = input('Type in password: ')
                if pass_input not in pass_col:
                    print('\nIncorrect password. Please try again.\n')
                    login_user()
                elif login_col.index(login_input) != pass_col.index(pass_input):
                    print('\nIncorrect password. Please try again.\n')
                    login_user()
                else:
                    clear_console()
                    print('\nLogin successful!\n\n')
                    how_to()
            return
        except ValueError():
            print('Invalid data. Please try again.')

def clear_console():
    """
    Clear the console.
    """
    clear = os.system('clear')

def how_to():
    """
    Show 'How to' text and show the logged in menu.
    """
    print('=' * 90)
    print('\nHow to:')
    print('\nEnter 2, 3 or 4 numbers, separated by comma.')
    print('\nDepending on your input, the programm will request next batch of numbers - 2, 3 or 4.')
    print('\nFor example, if you entered 3, then the program will request 3 more numbers 2 more times.')
    print('\nThen the program will return the matrix and its determinant.')
    print('\nExample:\n')
    print(colors.GREEN + '   3   4   5')
    print(colors.GREEN + '   0   8   1')
    print(colors.GREEN + '   9   7   6')
    print(colors.WHITE + '   \nThe matrix determinant is: -201')
    print('=' * 90)
    logged_in_menu()

def logged_in_menu():
    """
    Call the matrix building function or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - start")
    print("2 - return to the main screen")
    logged_input = input()
    if logged_input == "1":
        build()
    elif logged_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {logged_input}. Please enter 1 or 2.")
        logged_in_menu()

def build():
    """
    Pull data from matrix class and build the matrix.
    """      
    build_matrix = Matrix(start())
    arr = build_matrix.built_matrix()
    arr = arr.split()
    print(f"\nHere is your {len(build_matrix.row)}x{len(build_matrix.row)} matrix:\n")
    for i in range(len(arr)):
        print(colors.GREEN + "      " + arr[i].replace("[", "").replace("'", "").replace(",", "   ").replace("]", ""))

def start():
    """
    Get the list of numbers.
    """
    clear_console()
    print('\n\nStarting...')
    print('\nReady!')
    matrix = []
    while True:
        print('\nEnter 2, 3 or 4 numbers, separated by comma:')
        matrix_input = input()
        matrix_data = matrix_input.split(',')
        if validate_first_input(matrix_data):
            matrix.append(matrix_input)
            while True:
                print(f"\nEnter another {len(matrix_data)} numbers:")
                next_input = input()
                next_data = next_input.split(',')
                if validate_next(matrix_data, next_data):
                    matrix.append(next_input)
                    if len(matrix) == len(matrix_data):
                        return matrix

def validate_first_input(values):
    """
    Validate the first input, whether 2, 3 or 4 numbers are entered.
    """
    try:
        [int(value) for value in values]
        if len(values) not in range(2, 5):
            print(f"\nNeed to enter 2, 3 or 4 numbers. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"{e}. Please try again.")
        return False

def validate_next(value1, value2):
    """
    Validate next after the first inputs.
    """
    try:
        [int(val1) for val1 in value1]
        [int(val2) for val2 in value2]
        if len(value1) != len(value2):
            print(f"\nNeed to enter {len(value1)} numbers. You entered: {len(value2)}")
        else:
            return True
    except ValueError as e:
        print(f"{e}. Please try again.")
        return False

welcome()