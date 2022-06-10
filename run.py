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
    WHITE = '\033[97m'

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
    Show 'How to' text.
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
    loggen_in_menu()

def loggen_in_menu():
    """
    Start calculations or return to main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - start")
    print("2 - return to the main screen")
    logged_input = input()
    if logged_input == "1":
        start()
    elif logged_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {logged_input}. Please enter 1 or 2.")
        loggen_in_menu()

def start():
    """
    Define and build the matrix.
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
                if len(matrix_data) == 2:
                    matrix.extend(matrix_2x2(matrix_input))
                    return matrix
                elif len(matrix_data) == 3:
                    matrix.extend(matrix_3x3(matrix_input))
                    return matrix
                elif len(matrix_data) == 4:
                    matrix.extend(matrix_4x4(matrix_input))
                    return matrix

          
    
def res():
    var = start()
    print(var)
                
def matrix_2x2(two_x2):
    """
    Build 2x2 matrix.
    """
    while True:
        print('\nEnter another 2 numbers:')
        two_x2 = []
        row_2_2_input = input()
        row_2_2_data = row_2_2_input.split(',')
        if validate_row_2_2(row_2_2_data):
            two_x2.append(row_2_2_input)
            return two_x2

def matrix_3x3(three_x3):
    """
    Build 3x3 matrix.
    """
    while True:
        print('\nEnter another 3 numbers:')
        three_x3 = []
        row_2_3_input = input()
        row_2_3_data = row_2_3_input.split(',')
        if validate_matrix_x3(row_2_3_data):
            three_x3.append(row_2_3_input)
            while True:
                print('\nEnter final 3 numbers:')
                row_3_3_input = input()
                row_3_3_data = row_3_3_input.split(',')
                if validate_matrix_x3(row_3_3_data):
                    three_x3.append(row_3_3_input)
                    return three_x3

def matrix_4x4(four_x4):
    """
    Build 4x4 matrix.
    """
    while True:
        print('\nEnter another 4 numbers:')
        four_x4 = []
        row_2_4_input = input()
        row_2_4_data = row_2_4_input.split(',')
        if validate_matrix_x4(row_2_4_data):
            four_x4.append(row_2_4_input)
            while True:
                print('\nEnter another 4 numbers:')
                row_3_4_input = input()
                row_3_4_data = row_3_4_input.split(',')
                if validate_matrix_x4(row_3_4_data):
                    four_x4.append(row_3_4_input)
                    while True:
                        print('\nEnter final 4 numbers:')
                        row_4_4_input = input()
                        row_4_4_data = row_4_4_input.split(',')
                        if validate_matrix_x4(row_4_4_data):
                            four_x4.append(row_4_4_input)
                            return four_x4

def validate_first_input(values):
    """
    Validate the first input, if 2, 3 or 4 numbers are entered.
    """
    try:
        [int(value) for value in values]
        if len(values) not in range(2, 5):
            print(f"\nNeed to enter 2, 3 or 4 numbers. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False

def validate_row_2_2(values):
    """
    Validate the second input with 2 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 2:
            print(f"\nNeed to enter 2 numbers. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False

def validate_matrix_x3(values):
    """
    Validate the second input with 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            print(f"\nNeed to enter 3 numbers. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False

def validate_matrix_x4(values):
    """
    Validate the second input with 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            print(f"\nNeed to enter 4 numbers. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False

class Matrix:
    """
    Matrix class.
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

welcome()