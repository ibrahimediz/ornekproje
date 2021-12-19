from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random as rnd
import string

def passwordGenerator(max_len):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    rand_lower = rnd.choice(ascii_lowercase)
    rand_upper = rnd.choice(ascii_uppercase)
    rand_punc = rnd.choice(punctuation)
    rand_digits = rnd.choice(digits)
    
    password = rand_digits + rand_lower + rand_punc + rand_upper
    for x in range(max_len):
        password = password + rnd.choice(characters)
    print(password)

passwordGenerator(6)