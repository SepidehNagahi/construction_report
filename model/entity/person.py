from construction_report.model.entity import *
from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Boolean, DateTime


class Person(Base):
    __tablename__ = "person_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    family = Column(String(30))

    users = relationship("User", back_populates="person")
    daily_reports = relationship("DailyReport", back_populates="person")
    inventories = relationship("Inventory", back_populates="person")
    monthly_reports = relationship("MonthlyReport", back_populates="person")
    warehouses = relationship("Warehouse", back_populates="person")
    workers1 = relationship("Workers", back_populates="person")

    def __init__(self, name, family):
        self.id = None
        self.name = name
        self.family = family

    # def get_name(self):
    #     return self._name
    #
    # def set_name(self, name):
    #     self._name = Validator.name_validator(name, "Invalid Name")
    #
    # def get_family(self):
    #     return self._family
    #
    # def set_family(self, family):
    #     self._family = Validator.name_validator(family, "Invalid Family")
    #
    #
    # name = property(get_name, set_name)
    # family = property(get_family, set_family)
