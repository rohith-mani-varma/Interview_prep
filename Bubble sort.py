array = [64, 34, 25, 12, 22, 11, 90]

is_sorted = False

while not is_sorted:
    is_sorted = True
    size_of_array = len(array)
    for i in range(size_of_array-1):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i]= array[i+1]
            array[i+1]=temp
            is_sorted = False
print(array)

