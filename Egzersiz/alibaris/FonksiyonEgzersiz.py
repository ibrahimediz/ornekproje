"""
yukarıdaki kodlardan yardım alarak belirtilen uzunlukta aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az bir büyük harf
2. en az bir küçük harf
3. en az bir noktalama işareti
4. en az bir rakam 
5. karakter sınırı parametre olarak alınabilir
"""
from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random as rnd

def get_element(fun_name):
    if fun_name == "ascii_lowercase":
        return rnd.choice(ascii_lowercase)
    elif fun_name == "ascii_uppercase":
        return rnd.choice(ascii_uppercase)
    elif fun_name == "punctuation":
        return rnd.choice(punctuation)
    else:
        return rnd.choice(digits)


def generate_password(pass_len):
    passw = []

    while(len(passw) <= pass_len):
        funcs = ["ascii_lowercase","ascii_uppercase","punctuation","digits"]
        choice_funcs = rnd.choice(funcs)
        
        passw.append(get_element(choice_funcs))

    return "".join(passw)

pass_len = int(input("Enter pass len: "))
print(generate_password((pass_len)))

