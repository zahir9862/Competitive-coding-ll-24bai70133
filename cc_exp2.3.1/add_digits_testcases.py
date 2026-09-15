def addDigits(num):

    if num == 0:
        return 0

    return 1 + (num - 1) % 9


# Test Case 1
num = 38
print("Test Case 1")
print("Input =", num)
print("Answer =", addDigits(num))


# Test Case 2
num = 99
print("\nTest Case 2")
print("Input =", num)
print("Answer =", addDigits(num))


# Test Case 3
num = 12345
print("\nTest Case 3")
print("Input =", num)
print("Answer =", addDigits(num))


# Test Case 4
num = 0
print("\nTest Case 4")
print("Input =", num)
print("Answer =", addDigits(num))