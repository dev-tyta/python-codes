from sign_up import user_name, confirm_password
from game import get_input2

while True:
    print("User Login Page")
    username = input("Input username: ")
    password = input("Enter Password: ")

    if username == user_name:
        if password == confirm_password:
            break
        else:
            print("Wrong Password! Retry.....")
    else:
        print("Wrong Username!!! Retry")
print("Welcome!!!!")
get_input2()
