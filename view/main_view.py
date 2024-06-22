from tkinter import *


class MainView:
    def person_click(self):
        self.win.destroy()
        from construction_report.view import PersonView
        person_view = PersonView(self.user)

    def user_click(self):
        self.win.destroy()
        from construction_report.view import UserView
        user_view = UserView(self.user)

    def inventory_click(self):
        self.win.destroy()
        from construction_report.view import InventoryView
        inventory_view = InventoryView(self.user)

    def warehouse_click(self):
        self.win.destroy()
        from construction_report.view import WarehouseView
        warehouse_view = WarehouseView(self.user)

    def workers_click(self):
        self.win.destroy()
        from construction_report.view import WorkersView
        workers_view = WorkersView(self.user)

    def daily_report_click(self):
        self.win.destroy()
        from construction_report.view import DailyReportView
        daily_report_view = DailyReportView(self.user)

    def monthly_report_click(self):
        self.win.destroy()
        from construction_report.view import MonthlyReportView
        monthly_report_view = MonthlyReportView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.geometry("260x450")
        self.win.title("Construction Report App")
        # Label(text=user.person.name + " " + user.person.family, font=("Arial", 16)).place(x=50, y=5)

        Button(self.win, text="Profile", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.user_click).place(x=50, y=40)
        Button(self.win, text="Inventory", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.inventory_click).place(x=50, y=100)
        Button(self.win, text="Warehouse", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.warehouse_click).place(x=50, y=160)
        Button(self.win, text="Workers", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.workers_click).place(x=50, y=220)
        Button(self.win, text="Daily Report", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.daily_report_click).place(x=50, y=280)
        Button(self.win, text="Monthly Report", width=15, bg="lightgray", height=2, font=("Arial", 13),
               command=self.monthly_report_click).place(x=50, y=340)

        self.win.mainloop()

