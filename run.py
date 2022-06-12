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

class Matrix:
    """
    Matrix superclass.
    """
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def calc_2x2(self):
        return self.num1 * self.num4 - self.num2 * self.num3

class Matrix_2x2(Matrix):
    """
    2x2 matrix class,
    returns 2x2 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4):
        super().__init__(num1, num2, num3, num4)
    
    def determinant_2x2(self):
        return f'{super().calc_2x2()}'

class Matrix_3x3(Matrix):
    """
    3x3 matrix class,
    calculates 3x3 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, num8, num9):
        Matrix.__init__(self, num1, num2, num3, num4)
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
    
    def determinant_3x3(self):
        a = self.num1 * self.num5 * self.num9
        b = self.num2 * self.num6 * self.num7
        c = self.num3 * self.num4 * self.num8
        d = self.num3 * self.num5 * self.num7
        e = self.num2 * self.num4 * self.num9
        f = self.num1 * self.num6 * self.num8
        
        return a + b + c - d - e - f

class Matrix_4x4(Matrix):
    """
    4x4 matrix class,
    calculates 4x4 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16):
        Matrix.__init__(self, num1, num2, num3, num4)
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
        self.num10 = num10
        self.num11 = num11
        self.num12 = num12
        self.num13 = num13
        self.num14 = num14
        self.num15 = num15
        self.num16 = num16
    
    def determinant_4x4(self):
        a1 = self.num6 * self.num11 * self.num16
        b1 = self.num7 * self.num12 * self.num14
        c1 = self.num8 * self.num10 * self.num15
        d1 = self.num8 * self.num11 * self.num14
        e1 = self.num7 * self.num10 * self.num16
        f1 = self.num6 * self.num12 * self.num15

        a2 = self.num5 * self.num11 * self.num16
        b2 = self.num7 * self.num12 * self.num13
        c2 = self.num8 * self.num9 * self.num15
        d2 = self.num8 * self.num11 * self.num13
        e2 = self.num7 * self.num9 * self.num16
        f2 = self.num5 * self.num12 * self.num15

        a3 = self.num5 * self.num10 * self.num16
        b3 = self.num6 * self.num12 * self.num13
        c3 = self.num8 * self.num9 * self.num14
        d3 = self.num8 * self.num10 * self.num13
        e3 = self.num6 * self.num9 * self.num16
        f3 = self.num5 * self.num12 * self.num14

        a4 = self.num5 * self.num10 * self.num15
        b4 = self.num6 * self.num11 * self.num13
        c4 = self.num7 * self.num9 * self.num14
        d4 = self.num7 * self.num10 * self.num13
        e4 = self.num6 * self.num9 * self.num15
        f4 = self.num5 * self.num11 * self.num14
        
        m1 = self.num1 * (a1 + b1 + c1 - d1 - e1 - f1)
        m2 = self.num2 * (a2 + b2 + c2 - d2 - e2 - f2)
        m3 = self.num3 * (a3 + b3 + c3 - d3 - e3 - f3)
        m4 = self.num4 * (a4 + b4 + c4 - d4 - e4 - f4)

        return m1 - m2 + m3 - m4

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
    start_menu()

def start_menu():
    print('\n\nSelect one of the following options:')
    print("\n1 - create username")
    print("2 - login")
    start_input = input()
    if start_input == "1":
        clear_console()
        create_user()
    elif start_input == "2":
        clear_console()
        login_user()
    else:
        print(f"\nYou entered: {start_input}. Please enter 1 or 2.")
        start_menu()

def create_user():
    lo = []
    login = SHEET.worksheet('creds')
    login_col = login.col_values(1)
    new_user = input("Please type in a new username: ")
    if new_user in login_col:
        print("\nUsername already exist. Please enter another one.\n")
        create_user()
    else:
        lo.append(new_user)
        print(lo)
        return lo
    

create_user()

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
                print(f'No such user "{login_input}" exists.')
                retry_name()
            else:
                print('Username correct.\n')
                pass_input = input('Type in password: ')
                if pass_input not in pass_col:
                    print('\nIncorrect password.\n')
                    retry_pass()
                elif login_col.index(login_input) != pass_col.index(pass_input):
                    print('\nIncorrect password.\n')
                    retry_pass()
                else:
                    clear_console()
                    print('\nLogin successful!\n\n')
                    how_to()
            return
        except ValueError():
            print('Invalid data. Please try again.')

def retry_name():
    """
    Retry login if login is incorrect,
    or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - retry login")
    print("2 - return to the main screen")
    retry_name_input = input()
    if retry_name_input == "1":
        clear_console()
        login_user()
    elif retry_name_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {retry_name_input}. Please enter 1 or 2.")
        retry_name()

def retry_pass():
    """
    Retry login if password is incorrect,
    or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - retry login")
    print("2 - return to the main screen")
    retry_pass_input = input()
    if retry_pass_input == "1":
        clear_console()
        login_user()
    elif retry_pass_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {retry_pass_input}. Please enter 1 or 2.")
        retry_pass()

def clear_console():
    """
    Clear the console.
    """
    clear = os.system('clear')

def how_to():
    """
    Show 'How to' text and show the logged-in menu.
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
    Display the matrix and its determinant.
    """      
    build_matrix = start()
    print("\n" + "=" * 32)
    print(f"Here is your {len(build_matrix)}x{len(build_matrix)} matrix:\n")
    for i in range(len(build_matrix)):
        print(colors.GREEN + "      " + build_matrix[i].replace("[", "").replace("'", "").replace(",", "   ").replace("]", ""))
    array = str(build_matrix).replace("[", "").replace("'", "").replace("]", "")
    array = tuple(map(int, array.split(',')))
    if len(array) == 4:
        calc_2x2 = Matrix_2x2(array[0], array[1], array[2], array[3])
        print(colors.WHITE + f'\nThe matrix determinant is: {calc_2x2.determinant_2x2()}')
    if len(array) == 9:
        calc_3x3 = Matrix_3x3(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8])
        print(colors.WHITE + f'\nThe matrix determinant is: {calc_3x3.determinant_3x3()}')
    if len(array) == 16:
        calc_4x4 = Matrix_4x4(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11], array[12], array[13], array[14], array[15])
        print(colors.WHITE + f'\nThe matrix determinant is: {calc_4x4.determinant_4x4()}')
    print("=" * 32)
    try_again()

def try_again():
    print('\n\nSelect one of the following options:')
    print("\n1 - try again")
    print("2 - return to the main screen" + "\n" * 10)
    try_again_input = input()
    if try_again_input == "1":
        clear_console()
        build()
    elif try_again_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {try_again_input}. Please enter 1 or 2.")
        try_again()

def start():
    """
    Get the list of numbers depending on the first imput,
    i.e. amount of numbers entered in each input should match.
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

# welcome()