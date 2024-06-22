from construction_report.model.entity import *


class DailyReport(Base):
    __tablename__ = "daily_report_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    family = Column(String(30))
    presence = Column(Boolean)
    date = Column(DateTime)
    hour = Column(Integer)
    department = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    workers_id = Column(Integer, ForeignKey("workers_tbl.id"))
    workers = relationship("Workers")

    monthly_reports = relationship("MonthlyReport", back_populates="daily_report")

    def __init__(self, name, family, presence, date, hour, department):
        self.id = None
        self.name = name
        self.family = family
        self.presence = presence
        self.date = date
        self.hour = hour
        self.department = department
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
    # def get_date(self):
    #     return self._date
    #
    # def set_date(self, date):
    #     self._date = Validator.date_time_validator(date, "Invalid Date")
    #
    # def get_hour(self):
    #     return self._hour
    #
    # def set_hour(self, hour):
    #     self._hour = Validator.date_time_validator(hour, "Invalid Hour")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Department Name")
    #
    # name = property(get_name, set_name)
    # family = property(get_family, set_family)
    # date = property(get_date, set_date)
    # hour = property(get_hour, set_hour)
    # department = property(get_department, set_department)
