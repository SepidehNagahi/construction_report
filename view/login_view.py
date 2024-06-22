import tkinter.messagebox as msg
from tkinter import *

from construction_report.controller.user_controller import UserController
from construction_report.view.admin_view import AdminView
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.main_view import MainView


class LoginView:
    def login_click(self):

        ret, user = UserController.find_by_username_and_password(self.username.variable.get(),
                                                                 self.password.variable.get())
        if ret:
            # if user.role == "user":
            self.win.destroy()
            main_view = MainView(user)
            # elif user.role == "admin":
            #     self.win.destroy()
            #     admin_view = AdminView(user)
        else:
            msg.showerror("Login Error", "Access Denied !!!")

    def __init__(self):
        self.win = Tk()
        self.win.geometry("250x250")
        self.win.title("User")

        self.username = TextWithLabel(self.win, "Username", 20, 40)
        self.password = TextWithLabel(self.win, "Password", 20, 90)

        Button(self.win, text="Login", width=10, command=self.login_click).place(x=80, y=180)

        self.username.variable.set("sepideh")
        self.password.variable.set("sepideh123")

        self.win.mainloop()
