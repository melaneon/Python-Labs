#Melaniia Frolova
#A01391948
import lab4_login
import lab4_data_format

def main():
    first_name = input("Enter your first name: ").title()
    last_name = input("Enter your last name: ").title()
    user_id = input("Enter your BCIT ID: ")
    password = login.generate_login(first_name, last_name, user_id)
    print("Your password is: ", password)

    print('')
    print("PASSWORD RESET")
    new_password = login.change_password()
    print("Your new password is: ", new_password)

    print('')
    data_format.to_JSON_format(data_format.to_csv_format(data_format.get_book_info()))


if __name__ == "__main__":
    main()
