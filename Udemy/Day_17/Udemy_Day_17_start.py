class CarCrafting:
    # pass
    def __init__(self, id, username):
        print("New user registered...")
        self.id = id
        self.username = username
        self.seats = 5

    def race_mode(self):
        self.seats = 2


user_1 = CarCrafting("id", "Jo")
user_1.race_mode()

print(user_1.username)


def asd():
    pass
