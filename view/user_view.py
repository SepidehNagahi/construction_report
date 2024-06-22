import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkinter import *


from construction_report.controller.user_controller import UserController
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.table import Table
from construction_report.view.main_view import MainView


class UserView:
    def reset_form(self):
        self.id.variable.set("")
        self.username.variable.set("")
        self.password.variable.set("")
        self.department.variable.set("")
        # self.access.variable.set("")
        ret, user_list = UserController.find_all()
        if ret:
            self.table.refresh_table(user_list)

    def select_row(self, user):
        self.id.variable.set(user[0])
        self.username.variable.set(user[1])
        self.password.variable.set(user[2])
        self.department.variable.set(user[3])
        # self.access.set(user[4])

    def save_click(self):
        ret, message = UserController.save(self.username.variable.get(),
                                           self.password.variable.get(),
                                           self.department.variable.get(),
                                           self.access.get(),
                                           self.person_id.variable.get())
        if ret:
            msg.showinfo("Save User", "User Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        ret, message = UserController.edit(self.id.variable.get(),
                                           self.username.variable.get(),
                                           self.password.variable.get(),
                                           self.department.variable.get(),
                                           self.access.get(),
                                           self.person_id.variable.get())
        if ret:
            msg.showinfo("Edit User", "User Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        ret, message = UserController.remove(self.id.variable.get())
        if ret:
            msg.showinfo("Remove User", "User Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_username(self, event):
        ret, user_list = UserController.find_by_username(self.search_username.variable.get())
        if ret:
            self.table.refresh_table(user_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.win = Tk()
        self.user = user
        # Label(text=self.user.person.name + " " + self.user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.geometry("750x350")
        self.win.title("User")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.username = TextWithLabel(self.win, "Username", 20, 60)
        self.password = TextWithLabel(self.win, "Password", 20, 100)
        self.department = TextWithLabel(self.win, "Department", 20, 140)
        self.person_id = TextWithLabel(self.win, "Person_id", 20, 180, disabled=True)
        # self.person_id.variable.set(self.user.person)

        self.search_username = TextWithLabel(self.win, "Username", 350, 260)
        self.search_username.text_box.bind("<KeyRelease>", self.find_by_username)

        self.access = BooleanVar()
        ttk.Checkbutton(text='Access', variable=self.access).place(x=150, y=220)
        self.access.set(True)

        self.table = Table(self.win,
                           ["Id", "Username", "Password", "Department", "access"],
                           [60, 100, 110, 60, 60],
                           290,
                           20,
                           self.select_row)

        Button(self.win, text='Save', width=10,bg="green", command=self.save_click).place(x=30, y=260)
        Button(self.win, text='Edit', width=10,bg="gray", command=self.edit_click).place(x=135, y=260)
        Button(self.win, text='Remove', width=10,bg="red", command=self.remove_click).place(x=30, y=300)
        Button(self.win, text='Reset', width=10,bg="gray", command=self.reset_form).place(x=135, y=300)

        self.reset_form()

        self.win.mainloop()
