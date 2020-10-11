class Collective:
    # Коллектив влияет на оценку изменяя на 30% собственную оценку студента
    INFLUENCE = 0.3

    def __init__(self):
        self.students = []

    def calculate(self):
        avr = self.average()
        for i in self.students:
            if len(i.ratings) > 0:
                i.ratings[len(i.ratings) - 1] = \
                    int(i.ratings[len(i.ratings) - 1] * (1 - Collective.INFLUENCE) + Collective.INFLUENCE * avr)

    def average(self):
        sum = 0
        for i in self.students:
            if len(i.ratings) > 0:
                sum += i.ratings[len(i.ratings) - 1]
        return sum / len(self.students)
