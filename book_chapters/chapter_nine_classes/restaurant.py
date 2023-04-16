# restaurant class

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def get_name(self):
        return f"The restaurant name is {self.name}"

    def get_cuisine_type(self):
        return f"The cuisine type of the restaurant is {self.cuisine_type}"

    def set_number_server(self, number):
        self.number_served = number

    def increment_number_server(self, inc_number):
        self.number_served += inc_number


new_rest_1 = Restaurant('Open', 'Burgers')


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
            for flavor in self.flavors:
                print(flavor)


new_ice_cream = IceCreamStand('Ive', 'Ice cream')

new_ice_cream.flavors = ['plum', 'chocolatte', 'plombir']

print(new_ice_cream.show_flavors())