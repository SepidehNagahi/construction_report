from tkinter import *
import tkinter.messagebox as msg

from construction_report.controller.person_controller import PersonController
from construction_report.controller.user_controller import UserController
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.persian_calendar import PersianCalendar
from construction_report.view.component.table import Table
from construction_report.view.main_view import MainView


class PersonView:
    def reset_form(self):
        self.person_id.variable.set(self.user.person.person_id)
        self.name.variable.set(self.user.person.name)
        self.family.variable.set(self.user.person.family)
        self.user_id.variable.set(self.user.user_id)
        self.username.variable.set(self.user.username)
        self.password.variable.set(self.user.password)
        self.department.variable.set(self.user.department)

    def edit_click(self):
        person_status, message = PersonController.edit(self.person_id.variable.get(), self.name.variable.get(), self.family.variable.get())
        user_status, message = UserController.edit(self.user_id.variable.get(),
                                                   self.username.variable.get(),
                                                   self.password.variable.get(),
                                                   self.department.variable.get(),
                                                   self.user.access,
                                                   self.person_id.variable.get())
        if person_status and user_status:
            msg.showinfo("Edit Person", "Person Edited")
            self.reset_form()
            # self.user = UserController.find_by_id(self.user.user_id)
        else:
            msg.showerror("Edit Error", message)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()

        Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.geometry("250x370")
        self.win.title("Profile Person")

        self.person_id = TextWithLabel(self.win, "PersonId", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name", 20, 60)
        self.family = TextWithLabel(self.win, "Family", 20, 100)
        self.user_id = TextWithLabel(self.win, "UserId", 20, 180, disabled=True)
        self.username = TextWithLabel(self.win, "Username", 20, 220)
        self.password = TextWithLabel(self.win, "Password", 20, 260)
        self.department = TextWithLabel(self.win, "Department", 20, 300)

        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=80, y=320)

        self.reset_form()

        self.win.mainloop()

