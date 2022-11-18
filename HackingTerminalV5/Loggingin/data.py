import text, pickle

NAME = "Idiot-Terminal"
VERSION = "1.0.0"

USERS = {
    "qentang": "bigman15"
}

ADMINS = ["qentang", "raghuboi15", "ishetty123", "aaa"]

LOGGEDINUSER = ""


def CheckForNewUser():
    inp = input("Are you a new user (type y for yes or type anything for no): ")
    print()

    if inp == "y":

        while True:
            user = input("Choose a username: ")

            if user.lower() in USERS.keys():
                print("Username already taken, try again")
                continue

            user = user.replace(" ", "")

            password = input("Choose a password: ")
            confirm = input("Confirm your password: ")

            password = password.replace(" ", "")

            if password == confirm:
                print(f"\nRegistering your account ....\n"
                      f"User: {user}\n"
                      f"Password: {password}\n", end="\n\n")
                USERS[user.lower()] = password
                break
            else:
                print("Passwords do not match, press enter to try again")
                input()


def CheckForLogin():
    global LOGGEDINUSER
    while True:
        username = input(text.Indent("Enter a username: ", 5))
        password = input(text.Indent("Enter a password: ", 5))

        if username.lower() not in USERS.keys():
            print(f"Invalid username, try again", end="\n\n")
            continue

        if USERS[username.lower()] == password:
            LOGGEDINUSER = username

            if username.lower() == "qentang":
                print(f"Hello my lord, you shall gain access to your brilliant hacking terminal", end="\n\n")
                break
            print(f"Log in success, you may use the {NAME}", end="\n\n")
            break
        else:
            print(f"Log in failed, try logging in again", end="\n\n")


def LoadUsers():
    global USERS
    with open("users.dat", "rb") as f:
        try:
            USERS = pickle.load(f)
        except EOFError:
            USERS = {}


def SaveUsers():
    with open("users.dat", "wb") as f:
        pickle.dump(USERS, f)
