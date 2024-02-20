# 12) Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [[1], [2, 3], [4, [5, 6,[4,[9,[0]]]]]]
flat_list = flatten(nested_list)
print(flat_list)
