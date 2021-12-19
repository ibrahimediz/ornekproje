txt = input("Kelimeyi Giriniz: ")
txtList = [i for i in txt]
txtSet = set(txtList)

dictionary = dict()
for character in list(txtSet):
    dictionary[character] = txtList.count(character)

print(dictionary)
