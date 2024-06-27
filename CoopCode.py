
num = int(input())
has_seven = False

while num != 0:
    last_dig = num % 10

    if last_dig == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print("a")
else:
    print("b")