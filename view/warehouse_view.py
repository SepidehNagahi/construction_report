from tkinter import *
import tkinter.messagebox as msg

from datetime import datetime

from construction_report.view.main_view import MainView
from construction_report.view.component.persian_calendar import PersianCalendar
from construction_report.view.component.label_text import TextWithLabel
from construction_report.view.component.table import Table
from construction_report.controller.warehouse_controller import WarehouseController


class WarehouseView:
    def select_row(self, warehouse):
        self.id.variable.set(warehouse[0])
        self.title.variable.set(warehouse[1])
        self.unit.variable.set(warehouse[2])
        self.quantity.variable.set(warehouse[3])
        self.department.variable.set(warehouse[4])

    def reset_form(self):
        self.id.variable.set("")
        self.title.variable.set("")
        self.unit.variable.set("")
        self.quantity.variable.set("")
        self.department.variable.set("")
        status, warehouse_list = WarehouseController.find_all()
        if status:
            self.table.refresh_table(warehouse_list)

    def save_click(self):
        status, message = WarehouseController.save(self.title.variable.get(),
                                                   self.unit.variable.get(),
                                                   self.quantity.variable.get(),
                                                   self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "warehouse saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = WarehouseController.edit(self.id.variable.get(),
                                                   self.title.variable.get(),
                                                   self.unit.variable.get(),
                                                   self.quantity.variable.get(),
                                                   self.department.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "warehouse edited successfully!")
        else:
            msg.showerror("Error", message)

    def remove_click(self):
        status, message = WarehouseController.remove(self.id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "warehouse deleted successfully!")
        else:
            msg.showerror("Error", message)

    def search_by_id(self, event):
        if self.search_id.variable.get():
            status, warehouse_list = WarehouseController.find_by_id(self.search_id.variable.get())
            if status:
                self.table.refresh_table([warehouse_list])
        else:
            status, warehouse_list = WarehouseController.find_all()
            if status:
                self.table.refresh_table(warehouse_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        #Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.title('Warehouse')
        self.win.geometry('700x350')

        self.id = TextWithLabel(self.win, ' Id', 30, 60, 70, disabled=True)
        self.title = TextWithLabel(self.win, 'Title', 30, 100, 70)
        self.unit = TextWithLabel(self.win, 'Unit', 30, 140, 70)
        self.quantity = TextWithLabel(self.win, 'Quantity', 30, 180, 70)
        self.department = TextWithLabel(self.win, 'Department', 30, 220, 70)
        self.search_id = TextWithLabel(self.win, 'Search ID', 250, 280, 70)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(self.win,
                      [" Id", "Title", "Unit", "Quantity", "Department"],
                      [70, 90, 90, 90, 90,],
                      250,
                      20,
                      self.select_row)

        Button(self.win, text='Save', width=10,bg="green", command=self.save_click).place(x=30, y=260)
        Button(self.win, text='Edit', width=10,bg="gray", command=self.edit_click).place(x=135, y=260)
        Button(self.win, text='Remove', width=10,bg="red", command=self.remove_click).place(x=30, y=300)
        Button(self.win, text='Reset', width=10,bg="gray", command=self.reset_form).place(x=135, y=300)

        self.reset_form()

        self.win.mainloop()
