from model.Repository import groupNames
from model.student.Student import StudentBuilder



class StudentsGroup:

    # фабричный метод - паттерн
    @staticmethod
    def instance():
        temp = StudentsGroup()
        temp.name = groupNames()
        for i in range(0, 10):
            temp.students.append(StudentBuilder().addAppraisals().build())
        return temp

    def __init__(self):
        self.name = groupNames()
        self.students = []

    # отображение списка студентов и их оценов
    def evaluesList(self):
        for student in self.students:
            print(student.name)
            if student.ratings is not None:
                for rating in student.ratings:
                    print(rating)
            print('\n')
