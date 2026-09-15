def findDuplicate(nums):

    # Phase 1: Find meeting point
    slow = nums[0]
    fast = nums[0]

    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break


    # Phase 2: Find cycle entrance
    slow = nums[0]

    while slow != fast:

        slow = nums[slow]
        fast = nums[fast]

    return slow


# Test Case 1
nums = [1, 3, 4, 2, 2]

print("Test Case 1")
print("Array =", nums)
print("Duplicate =", findDuplicate(nums))


# Test Case 2
nums = [3, 1, 3, 4, 2]

print("\nTest Case 2")
print("Array =", nums)
print("Duplicate =", findDuplicate(nums))


# Test Case 3
nums = [3, 3, 3, 3, 3]

print("\nTest Case 3")
print("Array =", nums)
print("Duplicate =", findDuplicate(nums))


# Test Case 4
nums = [1, 1]

print("\nTest Case 4")
print("Array =", nums)
print("Duplicate =", findDuplicate(nums))