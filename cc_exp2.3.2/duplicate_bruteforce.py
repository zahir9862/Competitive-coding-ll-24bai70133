def findDuplicate(nums):

    seen = set()

    for x in nums:

        if x in seen:
            return x

        seen.add(x)

    return -1


nums = [1, 3, 4, 2, 2]

answer = findDuplicate(nums)

print("Brute Force Approach")
print("Array =", nums)
print("Duplicate =", answer)