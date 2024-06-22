from construction_report.model.da.data_access import *
from construction_report.model.entity.daily_report import DailyReport
from construction_report.model.tools.decorators import exception_handling


class DailyReportController:
    daily_report_da = DataAccess(DailyReport)

    @classmethod
    @exception_handling
    def save(cls, name, family, presence, date, hour, department):
        daily_report = DailyReport(name, family, presence, date, hour, department)
        return True, cls.daily_report_da.save(daily_report)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, presence, date, hour, department):
        daily_report = DailyReport(name, family, presence, date, hour, department)
        daily_report.id = id
        return True, cls.daily_report_da.edit(daily_report)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.daily_report_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.daily_report_da.find_all()

    @classmethod
    @exception_handling
    def find_by_department(cls, department):
        return True, cls.daily_report_da.find_by(DailyReport.department == department)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, cls.daily_report_da.find_by(DailyReport.family == family)

    @classmethod
    @exception_handling
    def find_by_date(cls, date):
        return True, cls.daily_report_da.find_by(DailyReport.date == date)

    @classmethod
    @exception_handling
    def find_by_name_and_family(cls, name, family):
        return True, cls.daily_report_da.find_by(and_(DailyReport.name == name, DailyReport.family == family))
