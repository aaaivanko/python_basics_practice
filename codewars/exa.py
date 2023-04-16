# def find_uniq(arr):
#     not_unique = 0
#     unique_item = 0
#     for item in arr:
#         if arr.count(item) > 1:
#             not_unique = item
#             break
#     new_set = set(arr)
#     new_arr = list(new_set)
#     for item in new_arr:
#         if item != not_unique:
#             unique_item = item
#     return unique_item
#
#
# def unique(some_list):
#     unique_el = [num for num in some_list if some_list.count(num) == 1]
#     return unique_el[0]
#
#
# def unique_the_simplest(arr):
#     return [num for num in arr if arr.count(num) == 1]
#
#
# print(unique_the_simplest([ 0, 0, 0.55, 0, 0 ]))
# print(unique_the_simplest([ 1, 1, 1, 2, 1, 1 ]))
# print(unique_the_simplest([ 3, 10, 3, 3, 3 ]))


def sorteddd(some_list):
    if some_list:
        return sorted(some_list)
    else:
        return []

