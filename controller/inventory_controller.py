from construction_report.model.da.data_access import *
from construction_report.model.entity.inventory import Inventory
from construction_report.model.tools.decorators import exception_handling


class InventoryController:
    inventory_da = DataAccess(Inventory)

    @classmethod
    @exception_handling
    def save(cls, title, unit, department):
        inventory = Inventory(title, unit, department)
        return True, cls.inventory_da.save(inventory)

    @classmethod
    @exception_handling
    def edit(cls, id, title, unit, department):
        inventory = Inventory(title, unit, department)
        inventory.id = id
        return True, cls.inventory_da.edit(inventory)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.inventory_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.inventory_da.find_all()

    @classmethod
    @exception_handling
    def find_by_department(cls, department):
        return True, cls.inventory_da.find_by(Inventory.department == department)

    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return True, cls.inventory_da.find_by(Inventory.title == title)

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.inventory_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_person_id(cls, person_id):
        return True, cls.inventory_da.find_by_person_id(person_id)
