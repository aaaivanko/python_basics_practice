# class with privileges

class Privileges:

    def __init__(self):
        self.privileges = ['add', 'remove', 'delete']

    def show_privileges(self):
        if not self.privileges:
            return None
        else:
            for priv in self.privileges:
                print(priv)