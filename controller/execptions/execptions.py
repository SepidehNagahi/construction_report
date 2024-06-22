class AccessDeniedError(Exception):
    def __init__(self):
        super().__init__("Wrong Username/Password !!!")


class NoUserFoundError(Exception):
    def __init__(self):
        super().__init__("No User Found !!!")


class DuplicateUsername(Exception):
    def __init__(self):
        super().__init__("Duplicate Username !!!")
