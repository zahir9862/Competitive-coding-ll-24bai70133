def findDuplicate(nums):

    # Phase 1
    slow = nums[0]
    fast = nums[0]

    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break


    # Phase 2
    slow = nums[0]

    while slow != fast:

        slow = nums[slow]
        fast = nums[fast]


    return slow


nums = [1, 3, 4, 2, 2]

answer = findDuplicate(nums)

print("Optimized Approach")
print("Array =", nums)
print("Duplicate =", answer)