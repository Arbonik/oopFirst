from model.StudentsGroup import StudentsGroup
from view.studentView import StudentView
import tkinter as tk


# Отображение группы
class GroupView:

    def __init__(self, studentGroup: StudentsGroup, root):
        self.studentGroup = studentGroup
        self.studentViews = list()

        self.root = root
        self.labelFrame = tk.LabelFrame(self.root, text=self.studentGroup.name)

        for student in studentGroup.students:
            studentRow = StudentView(student, self.labelFrame)
            self.studentViews.append(studentRow)

        self.labelFrame.pack()
