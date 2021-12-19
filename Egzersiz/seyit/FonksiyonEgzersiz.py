from string import ascii_lowercase,ascii_uppercase,punctuation,digits
print(ascii_lowercase,ascii_uppercase,punctuation,digits)
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd

def generate_pass(pass_len):
    pwd = ""
    for i in range(pass_len):
        rand_list = [rnd.choice(ascii_lowercase), rnd.choice(ascii_uppercase), \
                     rnd.choice(punctuation), rnd.choice( digits)]
        number = rnd.randint(0, 3)
        pwd += str(rand_list[number])

    return pwd


print(generate_pass(10))