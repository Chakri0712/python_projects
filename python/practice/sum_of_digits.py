a = int(input("Enter a number: "))
s = 0
for digit_str in str(a):
    digit = int(digit_str)
    s = s + (digit ** 3)

print(s)

