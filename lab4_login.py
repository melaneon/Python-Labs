#Melaniia Frolova
#A01391948

def generate_login(first_name, last_name, student_id):
    '''
    format first letter upper case and generate password
    using first three letter of the first name, first three letters of the last name
    and last three digits of the student ID number

    :param first_name: student first name
    :type first_name: str
    :param last_name: student last name
    :type last_name: str
    :param student_id: student BCIT id
    :type student_id: str

    :return: generated login password
    :rtype: str
    '''

    if len(first_name) > 3:
        password_part_1 = first_name[0:3]
    else:
        password_part_1 = first_name

    # format first letter upper case and
    # generate first three letter of the last name
    if len(last_name) > 3:
        password_part_2 = last_name[0:3]
    else:
        password_part_2 = last_name

    # generate last three symbols of the student ID
    if len(last_name) > 3:
        password_part_3 = student_id[-3:]
    else:
        password_part_3 = student_id

    # jam a full password
    login_password = password_part_1 + password_part_2 + password_part_3
    return login_password


def change_password():
    '''
    Password validation
    Must:
    - contain at least 7 symbols
    - not have any special characters
    - have at least one number
    - have at least one lower case letter
    - have at least one upper case letter

    :return: new validated password
    :rtype: str
    '''
    user_input = input("Enter a new password: ")


    while len(user_input) < 7 or user_input.isdigit() is True or user_input.isalnum() is False or user_input.isalpha() is True or user_input.lower() == user_input or user_input.upper() == user_input:
        if len(user_input) < 7:
            user_input = input("Password must be at least 7 characters. Try again: ")

        elif user_input.isdigit() is True:
            user_input = input("Password must include at least one character. Try again: ")

        elif user_input.isalpha() is True:
            if user_input.lower() == user_input:
                print("Password must include at least one upper case character and number")
                user_input = input("Try again: ")
                continue
            elif user_input.upper() == user_input:
                print("Password must include at least one lower case character and number")
                user_input = input("Try again: ")
                continue
            else:
                print("Password must include at least one number")
                user_input = input("Try again: ")
                continue

        elif user_input.isalnum() is False:
            if user_input.lower() == user_input:
                print("Password must include at least one upper case character and must not include special characters")
                user_input = input("Try again: ")
                continue
            elif user_input.upper() == user_input:
                print("Password must include at least one lower case character and must not include special characters")
                user_input = input("Try again: ")
                continue


        elif user_input.lower() == user_input:
            user_input = input("Password must include at least one upper case character. Try again: ")
        elif user_input.upper() == user_input:
            user_input = input("Password must include at least one lower case character. Try again: ")
        continue
    new_password = user_input
    return new_password




