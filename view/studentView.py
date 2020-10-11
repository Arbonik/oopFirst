import tkinter as tk
from model.student.Student import Student


# Отображение строки с именем студента и его оценками
class StudentView:

    def __init__(self, student: Student, root):
        self.student = student

        self.root = root
        self.studentFrame = tk.Frame(root)

        nameLabel = tk.Label(self.studentFrame, text=self.student.name)
        nameLabel.pack(side=tk.LEFT)

        # Список с оценками
        self.evalLabes = list()

        # Фрейм для оценок
        frame = tk.Frame(self.studentFrame)
        frame.pack(side=tk.RIGHT)

        if self.student.ratings is not None:
            for i in student.ratings:
                label = tk.Label(frame, text=i)
                label.pack(side=tk.LEFT)
                self.evalLabes.append(label)

        self.studentFrame.pack()
