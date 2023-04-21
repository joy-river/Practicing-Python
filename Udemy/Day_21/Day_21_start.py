#상속을 해보자
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("들숨 날숨")


class fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("퍼덕")

    def breathe(self):
        super().breathe()
        print("음파 음파")

nemo = fish()

nemo.breathe()
nemo.swim()