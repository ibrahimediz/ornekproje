import string
import random as rnd
from string import ascii_lowercase, ascii_uppercase,punctuation,digits

def random_password(len):
    
    source = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    pw = rnd.choice(string.ascii_lowercase)
    pw += rnd.choice(string.ascii_uppercase)
    pw += rnd.choice(string.punctuation)
    pw += rnd.choice(string.digits)

    for i in range(len):
        pw += rnd.choice(source)
    
    pw_ = list(pw)
    rnd.SystemRandom().shuffle(pw_)
    pw = ''.join(pw_)
    return pw

print(random_password(13)) 