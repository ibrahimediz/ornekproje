str1 = "YemekSepeti" #değişken tersten de indekslenmiştir
print(str1[-1]) #son elamanı verir
print(str1[-2]) #sondan birinci elamanı verir
print(str1[0:5]) #substring mantığı
print(str1[:5]) #baştan itibaren alacaksak
print(str1[5:]) #sona kadar gideceksek
print(str1[::-1]) #reverse string
print(str1[::2]) #indexleri 2 adımla gez

vary = "_________________aaa______YemekSepeti_______"
print(vary.strip('_a')) #baştan başlar parametre verilen elemanı temizler

vary1 = ["Yemek","Sepeti"]
print(";".join(vary1)) #listeden stringe dönüştürmek. split'in tersi gibi düşünülebilir


varlist = [1,5,6,7,8,1,1,10]
varlist.remove(1) #ilk gördüğü 1'i siler sonra bitirir
# veya
varlist = [el for el in varlist if el != 1] #tüm 1'ler uçtu. list comph


