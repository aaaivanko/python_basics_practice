# dict build mapping type key value pairs
# keys  immutable data types, values mutable
new_dict = {'name': 2, 'city': 3, 'age': 24}
new_dict_2 = {'colour': 'green', 'country': 'Poland', 'river': 'Dnipro'}
#
# for key, value in new_dict.items():
#     print(key, value)

# numb_dict = {'1': 1, '5': 5, '7': 7, '3': 3, '12': 12}
#
#
# def new_dict(some_dict):
#     if not some_dict:
#         return None
#     else:
#         max_value = max(some_dict.values())
#         for key, value in some_dict.items():
#             if value == max_value:
#                 max_key_value = f"{value} {key}"
#                 return max_key_value
#
#
# print(new_dict(numb_dict))

# swapped key value


# def swapped_dict(some_dict):
#     swapped = {}
#     if not some_dict:
#         return None
#     else:
#         for key, value in some_dict.items():
#             swapped[value] = key
#     return swapped
#
#
# print(swapped_dict(new_dict))

# new combined dict

# def comb_two_dict(first_dict, second_dict):
#     combined_dict = first_dict | second_dict
#     return combined_dict


# print(comb_two_dict(new_dict, new_dict_2))

# func in dict

# def mult(value):
#     return value ** 2
#
#
# def simple_dict(some_dict):
#     for key, value in new_dict.items():
#         some_dict[key] = mult(value)
#     return some_dict
#
#
# print(simple_dict(new_dict))

# dict_comp = {key + 'dd': value * 5 for key, value in new_dict.items()}
# print(dict_comp)

print(new_dict.get('gog'), 'No value assigned')