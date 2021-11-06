"""
ok this was from yesterday's Homework. So I didn't have to do much really. 
"""
def findValueSortedShiftedArray(nums, target):
    min = 0
    max = len(nums) - 1

    while not max < min:
        speculation = (max + min) // 2
        if nums[speculation] == target:
            return speculation
        elif nums[min] <= nums[speculation]:
            if nums[min] <= target < nums[speculation]:
                max = speculation
            else:
                min = speculation + 1
        else:
            print('min is greater than or equal to speculation')
            if nums[max - 1] >= target > nums[speculation]:
                min = speculation + 1
            else:
                max = speculation

    return -1

print(findValueSortedShiftedArray([4, 5, 6, 7, 0, 1, 2], 0))
print(findValueSortedShiftedArray([4,5,6,7,0,1,2], target = 3))