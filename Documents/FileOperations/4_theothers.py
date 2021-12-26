"""
json
csv
shelv
"""
import csv
import tabulate
with open("heart.csv") as dosya:
    liste = []
    csvOkuma = csv.reader(dosya,delimiter=",")
    for satir in csvOkuma:
        liste.append(satir)
basliklar = liste[0]
tb = tabulate.tabulate(liste[1:5])
print(tb)


with open("heartsKopya.csv","w") as dosya:
    liste = []
    csvyazma = csv.writer(dosya,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csvyazma.writerow(basliklar)
    csvyazma.writerow([45,25,65,85,74,22,45])
    # csvyazma.writerows(rows)

basliklar = ["Adı","Soyadı","Telefon"]
with open("TelDefter.csv","w") as dosya:
    sozlukYazar = csv.DictWriter(dosya,basliklar,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    sozlukYazar.writeheader()
    sozlukYazar.writerow({"Adı":"İbrahim","Soyadı":"Jamiryo","Telefon":"55555555555"})