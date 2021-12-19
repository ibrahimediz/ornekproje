# aci1 = input("1. Açıyı Giriniz:")
# aci2 = input("2. Açıyı Giriniz:")
# if (aci1 and aci2) and (aci1.isdigit() and aci2.isdigit()):
#     aci1,aci2 = int(aci1),int(aci2)
#     liste = [aci1,aci2,(180-(aci1+aci2))]
#     if sum(liste) == 180:
#         if len(set(liste)) == 2:
#             print("İkizkenar üçgen")
#         if len(set(liste)) == 3:
#             print("Çeşitkenar üçgen")
#         if 90 in liste:
#             print("Dik Üçgen")
#         if len(set(liste)) == 1:
#             print("Eşkenar Üçgen")
#     else:
#         print("Açı Hatası")
# else:
#     print("Giriş Hatası")


############################## Çözüm 1
def fun(sentence):
    result = dict()
    set_sentence = set(sentence)

    for c in set_sentence:
        result.setdefault(c, sentence.count(c))

    return result


var_input = input("Enter a sentence or word: ")
print(fun(var_input))

######################## Çözüm 2
text = 'afyonkarahisarlilastiramadiklarimizdanmisiniz'

letterCount = {}

for letter in text:
    if letter not in letterCount:
        if letter == ' ':
            letterCount['space'] = 1
        else:
            letterCount[letter] = 1
    else:
        if letter == ' ':
            letterCount['space'] = letterCount['space'] + 1
        else:
            letterCount[letter] = letterCount[letter] + 1

print(letterCount)
#########################Çözüm 3
dict_ = {}
text = input("Bir metin giriniz: ").lower()
for chr_ in text:
    dict_[chr_] = str(text.count(chr_))
print(dict_)
############################### 
text = 'afyonkarahisarlilastiramadikla     arimizdanmisiniz'
sozluk = {x:text.count(x) for x in text.replace(" ","") }
print(sozluk) 
