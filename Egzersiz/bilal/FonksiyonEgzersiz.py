from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random as rnd


kucuk = list(ascii_lowercase  + punctuation)
buyuk = list(ascii_uppercase 
noktalama =
sayi_ = list(digits)

def rastgele_sifre_uret():
	length = int(input("Uzunluk giriniz: "))
	rnd.shuffle(characters)
	password = []
	for i in range(length):
		password.append(rnd.choice(characters))

	rnd.shuffle(password)
	print("".join(password))


rastgele_sifre_uret()
