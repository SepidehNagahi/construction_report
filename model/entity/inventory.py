from construction_report.model.entity import *


class Inventory(Base):
    __tablename__ = "inventory_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    unit = Column(String(30))
    department = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    warehouses = relationship("Warehouse", back_populates="inventory")

    def __init__(self, title, unit, department):
        self.id = None
        self.title = title
        self.unit = unit
        self.department = department

    # def get_title(self):
    #     return self._title
    #
    # def set_title(self, title):
    #     self._title = Validator.name_validator(title, "Invalid Title")
    #
    # def get_unit(self):
    #     return self._unit
    #
    # def set_unit(self, unit):
    #     self._unit = Validator.name_validator(unit, "Invalid Unit")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Department Name")
    #
    # title = property(get_title, set_title)
    # unit = property(get_unit, set_unit)
    # department = property(get_department, set_department)
