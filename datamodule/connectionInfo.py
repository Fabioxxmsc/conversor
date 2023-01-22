
class ConnectionInfo:
    # __type = None
    __host: str
    __database: str
    __user: str
    __password: str

    def __init__(self):
        self.__host = ''
        self.__database = ''
        self.__user = ''
        self.__password = ''

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value