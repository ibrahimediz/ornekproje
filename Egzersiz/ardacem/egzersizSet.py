
# aci1 = input("1. aci giriniz:")
# aci2 = input("2. aci giriniz:")


################

str1 = str(input("String: "))

dict_ = {c:str1.count(c) for c in set(str1)}
print(dict_) # {'m': 1, 'e': 4, 'y': 1, 'k': 1, 'p': 1, 's': 1, 'i': 1, 't': 1}