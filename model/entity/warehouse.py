from construction_report.model.entity import *


class Warehouse(Base):
    __tablename__ = "warehouse_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    unit = Column(String(30))
    quantity = Column(Integer)
    department = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    inventory_id = Column(Integer, ForeignKey("inventory_tbl.id"))
    inventory = relationship("Inventory")

    def __init__(self, title, unit, quantity, department):
        self.id = None
        self.title = title
        self.unit = unit
        self.quantity = quantity
        self.department = department

    # def get_title(self):
    #     return self._title
    #
    # def set_title(self, title):
    #     self._title = Validator.name_validator(title, "Invalid Title")
    #
    # def get_code(self):
    #     return self._code
    #
    # def set_code(self, code):
    #     self._code = Validator.quantity_validator(code, "Invalid Code")
    #
    # def get_unit(self):
    #     return self._unit
    #
    # def set_unit(self, unit):
    #     self._unit = Validator.name_validator(unit, "Invalid Unit")
    #
    # def get_quantity(self):
    #     return self._quantity
    #
    # def set_quantity(self, quantity):
    #     self._quantity = Validator.quantity_validator(quantity, "Invalid Quantity")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Department Name")
    #
    # title = property(get_title, set_title)
    # code = property(get_code, set_code)
    # unit = property(get_unit, set_unit)
    # quantity = property(get_quantity, set_quantity)
    # department = property(get_department, set_department)
