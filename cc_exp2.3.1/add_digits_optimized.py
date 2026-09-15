def addDigits(num):

    # Special case
    if num == 0:
        return 0

    # Digital root formula
    return 1 + (num - 1) % 9


# Input
num = 38

# Function call
answer = addDigits(num)

# Output
print("Optimized Approach")
print("Input =", num)
print("Digital Root =", answer)