from random import Random

from model.Collective import Collective
from model.student.Student import Student


class University():
    def __init__(self):
        self.studentGroups = list()
        # коллективы
        self.collectives = [Collective(), Collective(), Collective()]

    # Все студенты получают оценки
    def anotherDay(self):
        for group in self.studentGroups:
            for student in group.students:
                student.addRating()
        for i in self.collectives:
            i.calculate()

    def addStudent(self, student: Student = Student()):
        self.studentGroups.append(student)

    # Вывод информации о студентах в консоль
    def show(self):
        for group in self.studentGroups:
            for student in group.students:
                student.show()

    def addToCollective(self, student :Student):
        self.collectives[Random().randint(0, len(self.collectives) - 1)].students.append(student)

    def thereWhere(self):
        for group in self.studentGroups:
            for student in group.students:
                self.addToCollective(student)