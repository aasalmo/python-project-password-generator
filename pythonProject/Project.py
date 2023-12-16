import string  # import String , random module
import random

# store all characters in list(upper/lower/digits/punctuation)
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# take number of charater from user
characters_numbers = input('how many character for the password? ')

# make sure that the number of charater is 6 or more
while True:
    try:
        characters_numbers = int(characters_numbers)
        if characters_numbers < 6:
            print('you need at least 6 characters')
            characters_numbers = input('how many character for the password? ')
        else:
            break
    except:
        print('please enter number only ')
        characters_numbers = input('how many character for the password? ')
# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
# calculate 30% and 20% of number of charcters
part1 = round(characters_numbers * (30 / 100))
part2 = round(characters_numbers * (20 / 100))
# create password 60% letters and 40% digits and punctuation
password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = ''.join(password[0:])
print(password)
