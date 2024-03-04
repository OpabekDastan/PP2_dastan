def check_all_true():
    x = int(input())
    my_list = []
    for i in range(x):
        my_list.append(input())
    thistuple = tuple(my_list)
    return all(thistuple)

result = check_all_true()
print(result)
