from construction_report.model.entity import *


class MonthlyReport(Base):
    __tablename__ = "monthly_report_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    family = Column(String(30))
    job = Column(String(30))
    number_of_days = Column(Integer)
    number_of_hours = Column(Integer)
    department = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    daily_report_id = Column(Integer, ForeignKey("daily_report_tbl.id"))
    daily_report = relationship("DailyReport")

    def __init__(self, name, family, job, number_of_days, number_of_hours, department):
        self.id = None
        self.name = name
        self.family = family
        self.job = job
        self.number_of_days = number_of_days
        self.number_of_hours = number_of_hours
        self.department = department

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
    # def get_job(self):
    #     return self._job
    #
    # def set_job(self, job):
    #     self._job = Validator.name_validator(job, "Invalid Job")
    #
    # def get_number_of_days(self):
    #     return self._number_of_days
    #
    # def set_number_of_days(self, number_of_days):
    #     self._number_of_days = Validator.date_time_validator(number_of_days, "Invalid Day")
    #
    # def get_number_of_hours(self):
    #     return self._number_of_hours
    #
    # def set_number_of_hours(self, number_of_hours):
    #     self._number_of_hours = Validator.date_time_validator(number_of_hours, "Invalid Hour")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Department Name")
    #
    # name = property(get_name, set_name)
    # family = property(get_family, set_family)
    # job = property(get_job, set_job)
    # number_of_days = property(get_number_of_days, set_number_of_days)
    # number_of_hours = property(get_number_of_hours, set_number_of_hours)
    # department = property(get_department, set_department)
