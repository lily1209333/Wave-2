import random
i = random.randint(0, 37)
nums = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26, 27,   28, 29, 30, 31, 32, 33, 34, 35, 36]
num = nums[i]
print("The spin resulted in", num, "...")
print("Pay", num)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
if num in red:
    print("Pay Red")
if num in black:
    print("Pay Black")
if num % 2 == 0 and num != 0 or num != 00:
    print("Pay Even")
if num % 2 == 1 and num != 0 or num != 00:
    print("Pay Odd")
if num < 19 and num > 0:
    print("Pay 1-18")
if num > 18:
    print("Pay 19-36")
