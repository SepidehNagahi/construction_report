from construction_report.model.da.data_access import *
from construction_report.model.entity.workers import Workers
from construction_report.model.tools.decorators import exception_handling


class WorkersController:
    workers_da = DataAccess(Workers)

    @classmethod
    @exception_handling
    def save(cls, name, family, job, daily_wages, hourly_wages, department):
        workers = Workers(name, family, job, daily_wages, hourly_wages, department)
        return True, cls.workers_da.save(workers)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, job, daily_wages, hourly_wages, department):
        workers = Workers(name, family, job, daily_wages, hourly_wages, department)
        workers.id = id
        return True, cls.workers_da.edit(workers)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.workers_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.workers_da.find_all()

    @classmethod
    @exception_handling
    def find_by_department(cls, department):
        return True, cls.workers_da.find_by(Workers.department == department)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, cls.workers_da.find_by(Workers.family == family)

    @classmethod
    @exception_handling
    def find_by_name_and_family(cls, name, family):
        return True, cls.workers_da.find_by(and_(Workers.name == name, Workers.family == family))

    @classmethod
    @exception_handling
    def find_by_person_id(cls, person_id):
        return True, cls.workers_da.find_by_person_id(person_id)
