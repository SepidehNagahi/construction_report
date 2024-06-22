from construction_report.model.entity import *


class Workers(Base):
    __tablename__ = "workers_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    family = Column(String(30))
    job = Column(String(30))
    daily_wages = Column(Integer)
    hourly_wages = Column(Integer)
    department = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    daily_reports = relationship("DailyReport", back_populates="workers")

    def __init__(self, name, family, job, daily_wages, hourly_wages, department):
        self.id = None
        self.name = name
        self.family = family
        self.job = job
        self.daily_wages = daily_wages
        self.hourly_wages = hourly_wages
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
    # def get_daily_wages(self):
    #     return self._daily_wages
    #
    # def set_daily_wages(self, daily_wages):
    #     self._daily_wages = Validator.date_time_validator(daily_wages, "Invalid Daily Wages")
    #
    # def get_hourly_wages(self):
    #     return self._hourly_wages
    #
    # def set_hourly_wages(self, hourly_wages):
    #     self._hourly_wages = Validator.date_time_validator(hourly_wages, "Invalid Hourly Wages")
    #
    # def get_department(self):
    #     return self._department
    #
    # def set_department(self, department):
    #     self._department = Validator.name_validator(department, "Invalid Group Name")
    #
    # name = property(get_name, set_name)
    # family = property(get_family, set_family)
    # job = property(get_job, set_job)
    # daily_wages = property(get_daily_wages, set_daily_wages)
    # hourly_wages = property(get_hourly_wages, set_hourly_wages)
    # department = property(get_department, set_department)
