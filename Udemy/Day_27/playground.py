def add(*args):
    print(args[1])
    print(args)


add(1, 2, 3, 4)

def cal(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

cal(4,  add= 3, multiply= 5)


class car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = car()