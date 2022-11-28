def bubble_sort(lst):
    for num in  range(len(lst) -1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]

    return lst

lst = [1, 4, 8, 2, 10, 5, 20, 3]
result = bubble_sort(lst)
print(result)


def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        midle = (high + low) // 2
        quess = lst[midle]
        if quess == search_item:
            search_res = True
            return search_res
        if quess > search_item:
            high = midle - 1
        else:
            low = midle + 1
    return search_res

lst = [1, 2, 4, 5, 6, 7, 8, 9]
find = 0
result = binary_search(lst, find)
print(result)
