from construction_report.model.da.data_access import *
from construction_report.model.entity.warehouse import Warehouse
from construction_report.model.tools.decorators import exception_handling


class WarehouseController:
    warehouse_da = DataAccess(Warehouse)

    @classmethod
    @exception_handling
    def save(cls, title, unit, quantity, department):
        warehouse = Warehouse(title, unit, quantity, department)
        return True, cls.warehouse_da.save(warehouse)

    @classmethod
    @exception_handling
    def edit(cls, id, title, unit, quantity, department):
        warehouse = Warehouse(title, unit, quantity, department)
        warehouse.id = id
        return True, cls.warehouse_da.edit(warehouse)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.warehouse_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.warehouse_da.find_all()

    @classmethod
    @exception_handling
    def find_by_department(cls, department):
        return True, cls.warehouse_da.find_by(Warehouse.department == department)

    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return True, cls.warehouse_da.find_by(Warehouse.title == title)


