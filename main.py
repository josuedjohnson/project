def encode(password):
    new_password = ""
    for i in password_input:
        new_password += str(int(i) + 3)

    return new_password

def decode(password):
    new_password = ""
    for i in password_input:
        new_password += str(int(i) - 3)

    return new_password

if __name__ == '__main__':
    password = ""
    og_pass = ""
    go = True
    while go:
        print("Menu\n-----------\n1. Encode\n2. Deocde\n3. Quit")
        choice = input("Please enter an Option")

        if choice == "1":
            password_input = input("Enter your password: ")
            og_pass = password_input
            new_password = encode(password_input)
            print("Encoded Password is ", new_password)
            print("Your password has been encoded and stored!")
            password = new_password

        if choice == "2":
            new_password = encode(password)
            print(f"The encoded password is {new_password}, and the original password is {og_pass}")