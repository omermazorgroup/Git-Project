from colorama import Fore
import sys


def password_check():
    """
     A program to validate password strength with the following requirements:
     password strength with the following requirements:
     Length – minimum of 10 characters.
     Contain both alphabet and number.
     Include both the small and capital case letters.
     The output will be green if it passed the validation and red if it didn’t.
     The program return exit code 0 if it passed the validation and exit code 1 if it didn’t.
    """
    try:
        passwd = str(sys.argv[1])
    except:
        passwd = ""
    errors = []
    if len(passwd) < 10:
        errors.append('length should be at least 10')

    if not any(char.isdigit() for char in passwd):
        errors.append('Password should have at least one numeral')

    if not any(char.islower() for char in passwd):
        errors.append('Password should have at least one lowercase letter')

    if not any(char.isupper() for char in passwd):
        errors.append('Password should have at least one uppercase letter')

    if len(errors) > 0:
        for error in errors:
            print(Fore.RED + error)
        print(Fore.RED + "Invalid Password !!")
        exit(1)
    else:
        print(Fore.GREEN + "Password is valid")
        exit(0)


password_check()
