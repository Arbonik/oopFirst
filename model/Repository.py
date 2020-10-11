import random

# Файл хранит функции генерации случайных имен для студентов и названий групп
firstname = ["Игорь", "Иван", "Надежда", "Любовь", "Василий", "Владислава", "Всеволод", "Ирина", "Олеся", "Евгения"]
lastname = ["Газман", "Зверь", "Мишинчук", "Левчук", "КакДела", "Мировлюб", "Четкич", "Такинов"]

groupNames = ["IT", "BIO", ]

def groupNames():
    return "group" + str(random.randint(1, 10)) + str(random.randint(0, 10)) + str(random.randint(1, 10))


def getRandomName():
    return firstname[random.randint(0, len(firstname) - 1)] + " " + lastname[random.randint(0, len(lastname) - 1)]

def getRandomGroup():
    return firstname[random.randint(0, len(firstname) - 1)] + " " + lastname[random.randint(0, len(lastname) - 1)]
