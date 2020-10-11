from model import Repository
from model.Location import Location


class Student:
    #   общее для всех стартовое значение способностей
    ability = 60

    # Создает случайного наследника класса Student
    @staticmethod
    def instance():
        import model.student.StudentChild
        rand = model.student.StudentChild.Random().randint(0, 3)
        if rand == 0:
            return model.student.StudentChild.Nerd()
        elif rand == 1:
            return model.student.StudentChild.Truant()
        elif rand == 2:
            return model.student.StudentChild.Lucky()
        elif rand == 3:
            return model.student.StudentChild.Freeloader()

    def __init__(self):
        # место жительства, выдается случайно
        self.location = Location.random()
        # отображение имени, типа студента, места жительства
        self.name = Repository.getRandomName() + " ("+ self.__class__.__name__ + ")\n" + str(self.location.name)
        # оценки студента
        self.ratings = list()
        # учебная группа студента
        self.studentGroup = None

    #     Модификатор живущего отдельно студента
        if self.location is Location.HOME:
            self.ability = self.ability + 10

    # расчет оценки, корректируется каждым наследником индивидуально
    def calculate(self):
        if self.location is Location.WITH_RELATIONS:
            return 10 + self.ability
        elif self.location is Location.DIRMOTORY:
            return 10 + self.ability

        return self.ability

    # добавление оценки в список
    def addRating(self):
        newRating = self.calculate()
        self.ratings.append(newRating)

    # отображение в консоли
    def show(self):
        temp = self.name
        if self.studentGroup is not None:
            temp += f" {self.studentGroup} "
        if type(self.ratings) is list:
            for i in self.ratings:
                temp += f" {i} "
        print(temp)


# паттерн строитель
class StudentBuilder:

    def __init__(self):
        self.student = Student.instance()

    def addAppraisals(self):
        # self.student.ratings = [50, 60, 70]
        return self

    def addGroup(self):
        from model.StudentsGroup import StudentsGroup
        self.student.studentGroup = StudentsGroup.instance()
        return self

    def build(self):
        return self.student
