import re


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def quantity_validator(cls, quantity, message):
        if isinstance(quantity, int) and quantity > 0:
            return quantity
        else:
            raise ValueError(message)

    @classmethod
    def date_time_validator(cls, year, month, day, hour, minute, second, message):
        try:
            return datetime(year, month, day, hour, minute, second)
        except ValueError:
            raise ValueError(message)
