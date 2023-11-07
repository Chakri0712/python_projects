import random
import string

Message = input("Enter a message: ")
Answer = input("What do you want to do?: ")
msg_length = len(Message)

def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    return random_string

random_string = generate_random_string(3)

def EncodeDecoder(Answer):
    if Answer == "encode":
        # code to execute when Answer is "code"
        if msg_length<3:
            reversed_string = Message[::-1]
            return reversed_string
        else:
            new_string = random_string + Message[1:] + Message[0] + random_string
            return new_string
    elif Answer == "decode":
        # code to execute when Answer is "decode"
         if msg_length<3:
            reversed_string = Message[::-1]
            return reversed_string
         else:
            result = Message[3:-3]
            new_string = result[-1] + result[:-1]
            return new_string
    else:
        return "Enter correct value"
    
value = EncodeDecoder(Answer)
print(value)