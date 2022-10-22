import sys
import getopt
import secrets
import string


def get_args(argv):
    # Global variable of the function
    arg_length = 12
    arg_special_char_bool = True
    arg_numbers_bool = True
    arg_help = "{0} -l <length> -s <special_char_bool> -n <numbers_bool>".format(argv[0])

    # Get args from user
    try:
        opts, args = getopt.getopt(argv[1:], "hl:s:n:", ["help", "length=", "special_char_bool=", "numbers_bool="])
    except:
        print("Wrong input, please use as below:\n")
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-l", "--length"):
            if int(arg) < 12:
                arg_length = 12
                print("The minimal length is set to 12, please don't input any lower value\n")
            else:
                arg_length = int(arg)
        elif opt in ("-s", "--special_char"):
            arg_special_char_bool = arg.lower()
        elif opt in ("-n", "numbers"):
            arg_numbers_bool = arg.lower()

    # Debug value
    # print('length:', arg_length)
    # print('special_char:', arg_special_char_bool)
    # print('numbers:', arg_numbers_bool)

    generate_password(arg_length, arg_special_char_bool, arg_numbers_bool)


def generate_password(arg_length, arg_special_char_bool, arg_numbers_bool):
    # Generate password
    final_string = string.ascii_letters
    password = ""

    if arg_special_char_bool == "true":
        final_string += string.punctuation

    if arg_numbers_bool == "true":
        final_string += string.digits

    for i in range(arg_length):
        password += secrets.choice(final_string)

    print("Here is your mighty password:", password)


if __name__ == "__main__":
    get_args(sys.argv)
