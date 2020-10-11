import tkinter as tk
from model.StudentsGroup import StudentsGroup, StudentBuilder
from view.groupView import GroupView
from model.University import University


class ControllerView:

    def addButtonUpdate(self, root):
        button = tk.Button(root, text="Итерация")
        button.config(command=self.updateAppenear)
        button.pack(side=tk.RIGHT)

    def addButtonGroup(self, root):
        button = tk.Button(root, text="Добавить группу")
        button.config(command=self.addGroup)
        button.pack(side=tk.RIGHT)

    def instanceInterface(self):
        frameInterface = tk.Frame(self.root)
        self.addButtonUpdate(frameInterface)
        self.addButtonGroup(frameInterface)
        frameInterface.pack(side=tk.BOTTOM)

    def addGroup(self):
        self.university.studentGroups.append(StudentsGroup.instance())
        self.university.thereWhere()
        self.updateUI()

    def updateAppenear(self):
        self.university.anotherDay()
        self.updateUI()

    def updateUI(self):
        # Очистка фреймов
        for i in self.root.winfo_children():
            i.destroy()
        # отображения групп
        for gr in self.university.studentGroups:
            self.viewGroup = GroupView(gr, self.root)
        # отображение интерфейса
        self.instanceInterface()
        self.root.mainloop()

    def __init__(self):
        self.root = tk.Tk()
        self.university = University()

        for gr in self.university.studentGroups:
            self.viewGroup = GroupView(gr, self.root)

        self.instanceInterface()

        self.university.show()

        self.root.mainloop()

