from tkinter import *
import tkinter.messagebox as msg
from datetime import datetime
from construction_report.view.main_view import MainView
from construction_report.view.component.persian_calendar import PersianCalendar
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.table import Table
from construction_report.controller.workers_controller import WorkersController


class WorkersView:
    def select_row(self, workers):
        self.id.variable.set(workers[0])
        self.name.variable.set(workers[1])
        self.family.variable.set(workers[2])
        self.job.variable.set(workers[3])
        self.daily_wages.variable.set(workers[4])
        self.hourly_wages.variable.set(workers[5])
        self.department.variable.set(workers[6])

    def reset_form(self):
        self.id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.job.variable.set("")
        self.daily_wages.variable.set("")
        self.hourly_wages.variable.set("")
        self.department.variable.set("")
        status, workers_list = WorkersController.find_all()
        if status:
            self.table.refresh_table(workers_list)

    def save_click(self):
        status, message = WorkersController.save(self.name.variable.get(),
                                                 self.family.variable.get(),
                                                 self.job.variable.get(),
                                                 self.daily_wages.variable.get(),
                                                 self.hourly_wages.variable.get(),
                                                 self.department.variable.get(),
                                                 self.person_id.variable.get())
        if status:
            msg.showinfo("Save", "workers saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = WorkersController.edit(self.id.variable.get(),
                                                 self.name.variable.get(),
                                                 self.family.variable.get(),
                                                 self.job.variable.get(),
                                                 self.daily_wages.variable.get(),
                                                 self.hourly_wages.variable.get(),
                                                 self.department.variable.get())
                                                 # self.person_id.variable.get())
        if status:
            msg.showinfo("Edit", "workers edited successfully!")
        else:
            msg.showerror("Error", message)

    def remove_click(self):
        status, message = WorkersController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove", "workers deleted successfully!")
        else:
            msg.showerror("Error", message)

    def search_by_id(self, event):
        if self.search_id.variable.get():
            status, workers_list = WorkersController.find_by_id(self.search_id.variable.get())
            if status:
                self.table.refresh_table([workers_list])
        else:
            status, workers_list = WorkersController.find_all()
            if status:
                self.table.refresh_table(workers_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        #Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.title('Workers')
        self.win.geometry('900x430')

        # self.workers_id = TextWithLabel(self.win, 'Person', 30, 20, 76, disabled=True)
        # self.workers_id.variable.set(f"{self.user.person_id}-{self.user.person.name}-{self.user.person.family}")

        self.id = TextWithLabel(self.win, ' Id', 30, 60, 76, disabled=True)
        self.name = TextWithLabel(self.win, 'Name', 30, 100, 76)
        self.family = TextWithLabel(self.win, 'Family', 30, 140, 76)
        self.job = TextWithLabel(self.win, 'Job', 30, 180, 76)
        self.daily_wages = TextWithLabel(self.win, 'Daily Wages', 30, 220, 76)
        self.hourly_wages = TextWithLabel(self.win, 'Hourly wages', 30, 260, 76)
        self.department = TextWithLabel(self.win, 'Department', 30, 300, 76)
        # self.person_id = TextWithLabel(self.win, "Person_id", 20, 370, disabled=True)
        # self.person_id.variable.set(self.workers.person.person_id)

        self.search_id = TextWithLabel(self.win, 'Search ID', 370, 270, 76)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(self.win,
                           ["Id", "Name", "Family", "Job", "Daily Wages", "Hourly wages", "Department"],
                           [70, 90, 90, 90, 90, 90, 90],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text='Save', width=10,bg="green", command=self.save_click).place(x=30, y=340)
        Button(self.win, text='Edit', width=10,bg="gray", command=self.edit_click).place(x=135, y=340)
        Button(self.win, text='Remove', width=10,bg="red", command=self.remove_click).place(x=30, y=380)
        Button(self.win, text='Reset', width=10,bg="gray", command=self.reset_form).place(x=135, y=380)

        self.reset_form()

        self.win.mainloop()
