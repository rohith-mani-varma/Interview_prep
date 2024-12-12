unsorted_array = [64, 25, 12, 22, 11]

for k in range(len(unsorted_array)):        
    for i in range(len(unsorted_array)):
        if unsorted_array[k] < unsorted_array[i]:
            min_element = unsorted_array[i]
            unsorted_array[i]= unsorted_array[k]
            unsorted_array[k]= min_element


print("sorted array  :", unsorted_array)