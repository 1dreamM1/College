class User:
    count = 0

    def __init__(self, name, login, password, level):
        self._name = name
        self._login = login
        self._password = password
        self._level = level
        if type(self) is User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return "********"
    
    @name.setter
    def name(self, value):
        self._name = value

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин")

    @password.setter
    def password(self, value):
        self._password = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")

    def __lt__(self, other):
        return self._level < other._level

    def __gt__(self, other):
        return self._level > other._level

    def __eq__(self, other):
        return self._level == other._level

    def __getattr__(self, item):
        print(f"Неизвестное свойство {item}")
        return " "

    def __setattr__(self, key, value):
        if key in ("_name", "name", "_login", "login", "_password", "password", "_level", "level"):
            super().__setattr__(key, value)
        else:
            print(f"Неизвестное свойство {key}")


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, admin, level):
        super().__init__(name, login, password, level)
        self._admin = admin
        if type(self) is SuperUser:
            SuperUser.count += 1

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, value):
        self._admin = value

    def __setattr__(self, key, value):
        if key in ("_name", "name", "_login", "login", "_password", "password", "_level", "level", "_admin", "admin"):
            super().__setattr__(key, value)
        else:
            print(f"Неизвестное свойство {key}")


user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10