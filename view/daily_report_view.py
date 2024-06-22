from tkinter import *
import tkinter.messagebox as msg

from datetime import datetime

from construction_report.view.main_view import MainView
from construction_report.view.component.persian_calendar import PersianCalendar
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.table import Table
from construction_report.controller.daily_report_controller import DailyReportController


class DailyReportView:
    def select_row(self, daily_report):
        self.id.variable.set(daily_report[0])
        self.name.variable.set(daily_report[1])
        self.family.variable.set(daily_report[2])
        self.presence.variable.set(daily_report[3])
        date_time = datetime.strptime(daily_report[4], "%Y-%m-%d")
        self.hour.variable.set(daily_report[5])
        self.department.variable.set(daily_report[6])

    def reset_form(self):
        self.id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.presence.variable.set("")
        self.hour.variable.set("")
        self.department.variable.set("")
        status, daily_report_list = DailyReportController.find_all()
        if status:
            self.table.refresh_table(daily_report_list)

    def save_click(self):
        status, message = DailyReportController.save(self.name.variable.get(),
                                                     self.family.variable.get(),
                                                     self.presence.variable.get(),
                                                     self.calendar.gregorian_date,
                                                     self.hour.variable.get(),
                                                     self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "daily_report saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = DailyReportController.edit(self.id.variable.get(),
                                                     self.name.variable.get(),
                                                     self.family.variable.get(),
                                                     self.presence.variable.get(),
                                                     self.calendar.gregorian_date,
                                                     self.hour.variable.get(),
                                                     self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "daily_report edited successfully!")
        else:
            msg.showerror("Error", message)

    def remove_click(self):
        status, message = DailyReportController.remove(self.id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "daily_report deleted successfully!")
        else:
            msg.showerror("Error", message)

    def search_by_id(self, event):
        if self.search_id.variable.get():
            status, daily_report_list = DailyReportController.find_by_id(self.search_id.variable.get())
            if status:
                self.table.refresh_table([daily_report_list])
        else:
            status, daily_report_list = DailyReportController.find_all()
            if status:
                self.table.refresh_table(daily_report_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        #Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.title('Daily Report')
        self.win.geometry('890x400')

        self.id = TextWithLabel(self.win, ' Id', 30, 60, 70, disabled=True)
        self.name = TextWithLabel(self.win, 'Name', 30, 100, 70)
        self.family = TextWithLabel(self.win, 'Family', 30, 140, 70)
        self.presence = TextWithLabel(self.win, 'presence', 30, 180, 70)
        Label(self.win, text="Date").place(x=30, y=220)
        self.calendar = PersianCalendar(self.win, 90, 220)
        self.hour = TextWithLabel(self.win, 'Hour', 30, 220, 70)
        self.department = TextWithLabel(self.win, 'department', 30, 260, 70)
        self.search_id = TextWithLabel(self.win, 'Search ID', 250, 280, 70)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(self.win,
                      [" Id", "Name", "Family", "Presence", "Date", "hour", "Department"],
                      [70, 90, 90, 90, 90, 90, 90],
                      250,
                      20,
                      self.select_row)

        Button(self.win, text='Save', width=10, bg="green", command=self.save_click).place(x=30, y=310)
        Button(self.win, text='Edit', width=10, bg="gray", command=self.edit_click).place(x=135, y=310)
        Button(self.win, text='Remove', width=10, bg="red", command=self.remove_click).place(x=30, y=350)
        Button(self.win, text='Reset', width=10, bg="gray", command=self.reset_form).place(x=135, y=350)

        self.reset_form()

        self.win.mainloop()

