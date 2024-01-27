try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero!")
finally:
    print("finally block executed")

try:
    x='hi'+1
except Exception as e:
    print(e)