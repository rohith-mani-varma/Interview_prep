numbers = [10, 20, 4, 45, 99, 99, 5]

def second_highest_num(nums):
    if len(nums)<2:
        return "No sufficient elements"
    first_highest = float('-inf')
    second_highest = float('-inf')

    for i in nums:
        if i>first_highest:
            second_highest = first_highest
            first_highest =i
        elif i> second_highest and i != first_highest:
            second_highest = i
    if second_highest == float('-inf'):
        return "No second highest found. "

    return second_highest

print(second_highest_num(numbers))