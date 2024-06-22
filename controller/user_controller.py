from construction_report.model.da.data_access import *
from construction_report.model.entity.user import User
from construction_report.model.tools.decorators import exception_handling


class UserController:
    user_da = DataAccess(User)

    @classmethod
    @exception_handling
    def save(cls, username, password, department, access):
        user = User(username, password, department, access)
        return True, cls.user_da.save(user)

    @classmethod
    @exception_handling
    def edit(cls, id, username, password, department, access):
        user = User(username, password, department, access)
        user.id = id
        return True, cls.user_da.edit(user)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.user_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.user_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.user_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, cls.user_da.find_by(User.username == username)


    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, cls.user_da.find_by(and_(User.username == username, User.password == password))
