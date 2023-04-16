from privileges import Privileges
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.logen_attempts = 0

    def describe_user(self):
        return f"{self.first_name} {self.last_name}"

    def greet_user(self):
        return f"Hello, {self.first_name}"

    def increment_login_attempts(self):
        self.logen_attempts += 1

    def reset_login_attempts(self):
        self.logen_attempts = 0


new_user = User('Bob', 'Oberkin')


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


new_admin = Admin('Bob', 'Oderkin')

print(new_admin.privileges.show_privileges())


