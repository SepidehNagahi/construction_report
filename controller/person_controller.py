from construction_report.model.da.data_access import *
from construction_report.model.entity.person import Person
from construction_report.model.tools.decorators import exception_handling
from construction_report.model.tools.logging import Logger


class PersonController:
    person_da = DataAccess(Person)

    @classmethod
    @exception_handling
    def save(cls, name, family):
        person = Person(name, family)
        return True, cls.person_da.save(person)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family):
        person = User(name, family)
        person.id = id
        return True, cls.person_da.edit(person)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.person_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.person_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.person_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, cls.person_da.find_by(Person.family == family)

    @classmethod
    @exception_handling
    def find_by_name_and_family(cls, name, family):
        return True, cls.user_da.find_by(and_(User.name == name, User.family == family))
