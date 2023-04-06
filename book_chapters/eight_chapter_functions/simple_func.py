
def items(*args, **kwargs):
    return args, kwargs


new_variable = items('many', 'folks', 14, name='Oleg', surname='Terry', age=42, city='Wroclaw', country='Poland')


# print(new_variable[1])

for key, value in new_variable[1].items():
    print(key, value)
