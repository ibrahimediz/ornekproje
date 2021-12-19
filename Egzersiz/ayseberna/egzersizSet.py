kelime = input("Kelime girin:")

for s in set(kelime):
    print(s , list(kelime).count(s))