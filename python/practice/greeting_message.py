import time

# print(type(time.strftime("%H")))
time_in_hours=int(time.strftime("%H"))
print(time_in_hours)
def message():
    if time_in_hours > 0 and time_in_hours < 12:
        return "Good morning!"
    elif time_in_hours >= 12 and time_in_hours < 16:
        return "Good afternoon!"
    else:
        return "Good evening!"


print(message())