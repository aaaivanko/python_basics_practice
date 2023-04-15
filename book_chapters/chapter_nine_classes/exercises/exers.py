# classes

class Dog:
    """Class about dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"The {self.name} is barking!"

    def god_age(self):
        return f"The dog is{self.age} years old."


new_dog = Dog('Ivan', 24)

print(new_dog.bark())
print(new_dog.god_age())
