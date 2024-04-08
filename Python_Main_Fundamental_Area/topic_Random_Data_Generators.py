import random
# todo Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import secrets
import string

m = []
print('\nExercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5')
for i in range(10):
    m.append(random.randrange(100, 199, 3))
print(sorted(m))
# todo Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets
#  from it as a winner.
print('\nExercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets'
      'from it as a winner.')
list_of_tickets = []
print("Creating 100 random lottery tickets")
# get 100 tickets
for i in range(100):
    list_of_tickets.append(random.randrange(1000000000, 9999999999))
# pic 2 random numbers
winners = random.sample(list_of_tickets, 2)
print("Lucky 2 lottery numbers are : ", winners)


# todo Exercise 3: Generate 6 digit random secure OTP
print('\nExercise 3: Generate 6 digit random secure OTP')
secrateGenerator = secrets.SystemRandom()
print("Generating 6 digits random OTP")
otp =secrateGenerator.randrange(100000, 999999)
print("Secure OTP is : ", otp)
# todo Exercise 4: Pick a random character from a given String
print('\nExercise 4: Pick a random character from a given String')
name = "Khosruzzaman"
print("Original String is : ", name)
char = random.choice(name)
print("Randomly picked char is :", char)

#todo Exercise 5: Generate random String of length 5
print('\nExercise 5: Generate random String of length 5')

def genStr(strLen):
    """Generate a random string of 5 chars"""
    latters = string.ascii_uppercase
    return "".join(random.choice(latters) for i in range(strLen))
print("Random string is ", genStr(5))

# TODO Exercise 6: Generate a random Password which meets the following conditions
print('\nExercise 6: Generate a random Password which meets the following conditions')
"""
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol."""
def random_pass(lengthOfPassword):
    latters = string.ascii_uppercase
    return
# Exercise 7: Calculate multiplication of two random float numbers
# Exercise 8: Generate random secure token of 64 bytes and random URL
# Exercise 9: Roll dice in such a way that every time you get the same number
# Exercise 10: Generate a random date between given start and end dates