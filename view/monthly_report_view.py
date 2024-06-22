from tkinter import *
import tkinter.messagebox as msg

from datetime import datetime

from construction_report.view.main_view import MainView
from construction_report.view.component.persian_calendar import PersianCalendar
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.table import Table
from construction_report.controller.monthly_report_controller import MonthlyReportController


class MonthlyReportView:
    def select_row(self, monthly_report):
        self.id.variable.set(monthly_report[0])
        self.name.variable.set(monthly_report[1])
        self.family.variable.set(monthly_report[2])
        self.job.variable.set(monthly_report[3])
        self.number_of_days.variable.set(monthly_report[4])
        self.number_of_hours.variable.set(monthly_report[5])
        self.department.variable.set(monthly_report[6])

    def reset_form(self):
        self.id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.job.variable.set("")
        self.number_of_days.variable.set("")
        self.number_of_hours.variable.set("")
        self.department.variable.set("")
        status, monthly_report_list = MonthlyReportController.find_all()
        if status:
            self.table.refresh_table(monthly_report_list)

    def save_click(self):
        status, message = MonthlyReportController.save(self.name.variable.get(),
                                                       self.family.variable.get(),
                                                       self.job.variable.get(),
                                                       self.number_of_days.variable.get(),
                                                       self.number_of_hours.variable.get(),
                                                       self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "monthly_report saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = MonthlyReportController.edit(self.id.variable.get(),
                                                       self.name.variable.get(),
                                                       self.family.variable.get(),
                                                       self.job.variable.get(),
                                                       self.number_of_days.variable.get(),
                                                       self.number_of_hours.variable.get(),
                                                       self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "monthly_report edited successfully!")
        else:
            msg.showerror("Error", message)

    def remove_click(self):
        status, message = MonthlyReportController.remove(self.id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "monthly_report deleted successfully!")
        else:
            msg.showerror("Error", message)

    def search_by_id(self, event):
        if self.search_id.variable.get():
            status, monthly_report_list = MonthlyReportController.find_by_id(self.search_id.variable.get())
            if status:
                self.table.refresh_table([monthly_report_list])
        else:
            status, monthly_report_list = MonthlyReportController.find_all()
            if status:
                self.table.refresh_table(monthly_report_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        #Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.title('Monthly Report')
        self.win.geometry('920x450')

        self.id = TextWithLabel(self.win, ' Id', 30, 60, 100, disabled=True)
        self.name = TextWithLabel(self.win, 'Name', 30, 100, 100)
        self.family = TextWithLabel(self.win, 'Family', 30, 140, 100)
        self.job = TextWithLabel(self.win, 'Job', 30, 180, 100)
        self.number_of_days = TextWithLabel(self.win, 'Number Of Days', 30, 220, 100)
        self.number_of_hours = TextWithLabel(self.win, 'Number Of Hours', 30, 260, 100)
        self.department = TextWithLabel(self.win, 'Department', 30, 300, 100)
        self.search_id = TextWithLabel(self.win, 'Search ID', 300, 300, 100)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(self.win,
                      [" Id", "Name", "Family", "Job","Number Of Days", "Number Of Hours", "Department"],
                      [70, 90, 90, 90, 90, 90, 90],
                      280,
                      50,
                      self.select_row)

        Button(self.win, text='Save', width=10,bg="green", command=self.save_click).place(x=30, y=360)
        Button(self.win, text='Edit', width=10,bg="gray", command=self.edit_click).place(x=135, y=360)
        Button(self.win, text='Remove', width=10,bg="red", command=self.remove_click).place(x=30, y=400)
        Button(self.win, text='Reset', width=10,bg="gray", command=self.reset_form).place(x=135, y=400)

        self.reset_form()

        self.win.mainloop()
