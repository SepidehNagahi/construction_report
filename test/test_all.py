from construction_report.model.da.data_access import DataAccess
from construction_report.model.entity.user import User
from construction_report.model.entity.person import Person
from construction_report.model.entity.daily_report import DailyReport
from construction_report.model.entity.inventory import Inventory
from construction_report.model.entity.monthly_report import MonthlyReport
from construction_report.model.entity.warehouse import Warehouse
from construction_report.model.entity.workers import Workers
#
from construction_report.controller.user_controller import UserController
from construction_report.controller.person_controller import PersonController
from construction_report.controller.inventory_controller import InventoryController
from construction_report.controller.warehouse_controller import WarehouseController
from construction_report.controller.daily_report_controller import DailyReportController
from construction_report.controller.workers_controller import WorkersController
from construction_report.controller.monthly_report_controller import MonthlyReportController
#
from construction_report.view.user_view import UserView
from construction_report.view.person_view import PersonView
from construction_report.view.daily_report_view import DailyReportView
from construction_report.view.monthly_report_view import MonthlyReportView
from construction_report.view.workers_view import WorkersController
from construction_report.view.inventory_view import InventoryView
from construction_report.view.warehouse_view import WarehouseView
# #
user_da = DataAccess(User)
person_da = DataAccess(Person)
daily_report_da = DataAccess(DailyReport)
inventory_da = DataAccess(Inventory)
monthly_report_da = DataAccess(MonthlyReport)
warehouse_da = DataAccess(Warehouse)
workers_da = DataAccess(Workers)

#
# TESTS PASSED


# person1 = Person("saba", "samavat")
# person_da.save(person1)
# # print(person1)
#
# person2 = Person("sepideh", "Nagahi")
# person_da.save(person2)
# print(person2)
#
# user1 = User("sepideh", "sepideh123", "tty", 1)
# user_da.save(user1)
# print(user1)
#
# user2 = User("ali", "ali123456", "hgh", 0)
# user_da.save(user2)
# print(user2)
#
# user3 = User("danial", "dani123456", "ppi", 1)
# user_da.save(user3)
# print(user3)

# UserController.edit(2, "ali", "ahmadi1234","ytyt",1)

# #
# workers1 = Workers("leila", "rezai", "far", 12, 3, "sad")
# workers_da.save(workers1)
# print(workers1)
#
#
# workers3 = Workers("hasan", "hasani", "mohandes", 5, 30, "sakhteman")
# workers_da.save(workers3)
# print(workers3)
#
# # # #
# warehouse1 = Warehouse("fani", "hdueh", 32, "fkjf")
# warehouse_da.save(warehouse1)
# print(warehouse1)
# #
# inventory1 = Inventory("fani", "ddd", "gad")
# inventory_da.save(inventory1)
# print(inventory1)
# inventory1 = Inventory("saba", "faf", "yuh")
# inventory_da.save(inventory1)
# # print(inventory1)
#
daily_report1 = DailyReport("sama", "samavat", 1, "2024-1-2", 2, "djwjd")
daily_report_da.save(daily_report1)
print(daily_report1)
#
# monthly_report1 = MonthlyReport("ziba", "zarif", "mohands", 365, 170, "dsd")
# monthly_report_da.save(monthly_report1)
# print(monthly_report1)
#
# workers_da = DataAccess(Workers)
# workers = Workers("salar", "aghili", "nasab", 2, 3, "err")
# workers.daily_report = DailyReport
# workers_da.save(workers)
# print(workers)

# ui = UserView()
