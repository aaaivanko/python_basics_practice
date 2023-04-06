# unique in order

new_str = 'ABBCcAD'

new_string_list = [*new_str]

new_list = [1, 4, 6, 7, 7, 3]


print(list(dict.fromkeys(new_list)))
print(list(dict.fromkeys(new_string_list)))