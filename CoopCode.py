
n = int(input())
count = 1
max_number = 0

while n != 0:
    number = n % 10
    number1 = n % 10

    if number > count:
        max_number = number

print(max_number)




