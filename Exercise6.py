
while True:              #made a while loop which will break once correct password is inputed
    password = (input("Enter the password: "))           
    if password == "12345":                    #made an if statement where it will print the correct statement when given the "12345" answer
        print("Welcome back, User.")
        break
    else:                  #else statement if the user gave a different answer than 12345, going back to the string input question
        print("Invalid Password. Try again.")