def addDigits(num):

    # Repeat until only one digit remains
    while num >= 10:

        total = 0

        # Add all digits
        while num > 0:
            total = total + (num % 10)
            num = num // 10

        num = total

    return num


# Input
num = 38

# Function call
answer = addDigits(num)

# Output
print("Brute Force Approach")
print("Input =", num)
print("Digital Root =", answer)