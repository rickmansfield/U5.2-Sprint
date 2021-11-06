def binarySearch(arr, key):
    min = 0
    max = len(arr) -1
    while not max < min:
        guess = (max+min) // 2
    
        if key == arr[guess]:
            return arr[guess]
        elif key > arr[guess]:
            min = guess + 1
        else: 
            max = guess - 1
    return -1

def findValueSortedShiftedArray(nums, target):
    pivot = 3
    if nums[pivot] == target:
        return pivot
    if nums[pivot] >= target:
        value = binarySearch(nums[pivot+1:],target)
        print(value)
        if value == target:
            return nums.index(value)
        

print("Answers", findValueSortedShiftedArray([4, 5, 6, 7, 0, 1, 2], 0))
print("Answers2", findValueSortedShiftedArray([4, 5, 6, 7, 0, 1, 2], 3))