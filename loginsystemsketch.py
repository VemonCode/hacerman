username = ""
loginUser = ""
password = ""
maxTries = 5
tries = 0

while username == "":
    username = input("Choose a username: ")
    if len(username) < 3:
        print("Please choose a username that has 3 or more characters.")
        username = ""

while password == "":
    password = input("Choose a password: ")
    if len(password) < 8:
        print("Please choose a password that has 8 or more characters.")
        password = ""

if tries < maxTries:
    while loginUser != username:
        loginUser = input("Enter your username. ")
    loginPass = input("Enter your password. ")
    if loginPass != password:
        tries += 1
    elif loginPass == password:
        print("Welcome Back, " + username + "!")
elif tries >= maxTries:
    print("The limit of attempts have been reached, try again another time.")
