n = int(input("Enter number: "))

power = len(str(n))   # count digits
temp = n
sum = 0

while temp > 0:
    digit = temp % 10        # get last digit
    sum += digit ** power    # raise to power and add
    temp = temp // 10        # remove last digit

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong")