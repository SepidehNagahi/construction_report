from construction_report.model.entity import *
from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Boolean, DateTime


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True)
    password = Column(String(20), nullable=False)
    department = Column(String(30), nullable=False)
    access = Column(Boolean)
    role = Column(String(10))

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    def __init__(self, username, password, department, access):
        self.id = None
        self.username = username
        self.password = password
        self.department = department
        self.access = access
        self.role = None
        self.person = None

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
    # def get_username(self):
    #     return self._username
    #
    # def set_username(self, username):
    #     self._username = Validator.username_validator(username, "Invalid Username")
    #
    # def get_password(self):
    #     return self._password
    #
    # def set_password(self, password):
    #     self._password = Validator.password_validator(password, "Invalid Password")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Department Name")
    #
    # name = property(get_name, set_name)
    # family = property(get_family, set_family)
    # username = property(get_username, set_username)
    # password = property(get_password, set_password)
    # department = property(get_department, set_department)
