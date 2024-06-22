from construction_report.model.da.data_access import *
from construction_report.model.entity.monthly_report import MonthlyReport
from construction_report.model.tools.decorators import exception_handling


class MonthlyReportController:
    monthly_report_da = DataAccess(MonthlyReport)

    @classmethod
    @exception_handling
    def save(cls, name, family, job, number_of_days, number_of_hours, department):
        monthly_report = MonthlyReport(name, family, job, number_of_days, number_of_hours, department)
        return True, cls.monthly_report_da.save(monthly_report)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, job, number_of_days, number_of_hours, department):
        monthly_report = MonthlyReport(name, family, job, number_of_days, number_of_hours, department)
        monthly_report.id = id
        return True, cls.monthly_report_da.edit(monthly_report)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.monthly_report_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.monthly_report_da.find_all()

    @classmethod
    @exception_handling
    def find_by_department(cls, department):
        return True, cls.monthly_report_da.find_by(MonthlyReport.department == department)

    @classmethod
    @exception_handling
    def find_by_name_and_family(cls, name, family):
        return True, cls.monthly_report_da.find_by(and_(MonthlyReport.name == name, MonthlyReport.family == family))
