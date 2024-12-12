lst = [1, 2, 2, 3, 4, 4, 5]

set = set(lst)

print(set)

lst = list(set)

print(lst)
unique_list= []
for num in lst:

    if num not in unique_list:
        unique_list.append(num)

print(unique_list)