
# fibonacci series
def Fibonacci(n):
    if n <= 1:
        return n;
    else:
       return Fibonacci(n-1)+Fibonacci(n-2)

n=int(input("Enter any number: "))

for i in range(n):
    print(Fibonacci(i))

# factorial
def Factorial(n):
    if n == 1:
        return n
    else:
        return n* Factorial(n-1)

f=int(input("Enter any number: "))
print(Factorial(f))