import game

print("""Sign-Up Page. 
    Welcome to the game input your details
""")
full_name = input("Input Full Name: ")
while True:
    user_name = input("Create aa username: ")
    password = input("Create a Password: ")
    if len(password) < 8:
        print("Password has to be 8 or more numbers.")
    else:
        confirm_password = input("Confirm Password: ")
        if confirm_password == password:
            break
        else:
            print("Password doesn't match")

print(f"Welcome {user_name}!!!!")
game.get_input()
