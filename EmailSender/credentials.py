# from typing import Final

# EMAIL: Final[str] = '**************'
# PASSWORD: Final[str] = '**************'


# Read credentials from a text file
def read_credentials_from_text_file(filename):
    credentials = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            credentials[key] = value
    return credentials

filename = 'credentials.txt'
credentials = read_credentials_from_text_file(filename)
Email = credentials.get('Email', '').strip("'\"")
Password = credentials.get('Password', '').strip("'\"")

print(Email)
print(Password)


