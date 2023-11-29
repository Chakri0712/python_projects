vowels = ['a', 'e', 'i', 'o', 'u']

character = input("Enter any character: ")

if character.lower() in vowels:
    print("vowel")
else:
    print("consonant")
