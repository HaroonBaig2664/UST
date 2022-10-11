num = 1456
reversed_num = 0

while num != 0:
    result = num % 10
    reversed_num = reversed_num * 10 + result
    num //= 10

print("Reversed Number: " + str(reversed_num))
