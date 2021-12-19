from string import ascii_lowercase,ascii_uppercase,punctuation,digits
#print(ascii_lowercase,ascii_uppercase,punctuation,digits)
import random as rnd

def pwOlustur(uzunluk):
    if(uzunluk>3):    
        password = rnd.choice(punctuation)
        password = password+ rnd.choice(digits)
        password = password+ rnd.choice(ascii_uppercase)
        password = password+ rnd.choice(ascii_lowercase)
        total = ascii_lowercase + ascii_uppercase + digits + punctuation
        add = "".join(rnd.sample(total,uzunluk-4))
        return password+add
    else:
        return "uzunluk min 4 olmalı"
