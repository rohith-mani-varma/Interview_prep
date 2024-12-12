arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

to_find = 65

low = 0
high = len(arr)-1
while low<=high:
    mid = (high+low)//2
    if arr[mid]==to_find:
        print("Found at index "+ str(mid))
        break
    elif arr[mid] > to_find:
        high = mid
    else: low = mid