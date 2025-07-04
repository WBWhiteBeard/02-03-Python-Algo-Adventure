

def removeElement(nums, val):

    slow = 0
    fast = 0
    while fast < len(nums):
        if (nums[slow] == val) and (nums[fast] == val):
            fast += 1
        elif (nums[slow] == val) and (nums[fast] != val):
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        elif (nums[slow] != val) and (nums[fast] == val):
            slow += 1
        else:
            slow += 1
            fast += 1
    return slow

nums = [3, 3, 3]
val = 5
print(removeElement(nums, val))

