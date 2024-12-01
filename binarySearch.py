# BINARY SEARCH
# Binary search is a searching algorithm that is used to find the
# target value from a sorted array.

def binary_search(sequence, item):
    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:
        mid_point = start_index + (end_index - start_index) // 2
        mid_value = sequence[mid_point]
        if item == mid_value:
            return mid_point
        elif item < mid_value:
            end_index = mid_point - 1
        else:
            start_index = mid_point + 1

    return None

sequence_a = [2,4,8,10,16,30,45]
item_a = 45
print("Item is present at index: ",binary_search(sequence_a, item_a))