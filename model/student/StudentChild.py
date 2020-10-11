from random import Random
from model.student.Student import Student


# заучка
class Nerd(Student):
    def calculate(self):
        return 10 + super().calculate()


# Прогульщик
class Truant(Student):
    def calculate(self):
        return super().calculate() - 10


# Везунчик
class Lucky(Student):
    def calculate(self):
        return Random().randint(0, 10) + super().calculate()


# Халявщик
class Freeloader(Student):
    def calculate(self):
        return super().calculate() - Random().randint(0,10)
