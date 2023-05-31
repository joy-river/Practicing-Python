
class User:
    def __init__(self):
        self.firstname = input("Welcome to the Flighter.\nRegister to get a useful travel information!\nWhat is your first name?\n")
        self.lastname = input("What is your last name?\n")
        self.email = input("What is your email?\n")
        self.valid = input("Please type your email again\n") == self.email
        while not self.valid:
            self.valid = input("Wrong email. Please type again\n") == self.email
        print("Welcome you! Now You're in the Flighter!")