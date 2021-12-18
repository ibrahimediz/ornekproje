# """
# var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın 
# Yukarıdaki çıktıyı almak için gereken python kodunu yazınız. 
# """
# # handy
# var1 = "Teşekkürler Süpermen"
# print(var1[::-1].replace('e', 'i',2)[::-1])

# # second way
# var1 = "Teşekkürler Süpermen"
# var2 = var1.replace("Süpermen",var1.split()[1].replace("e", "ı"))


"""
TC kimlik numarasi Algoritmanın kuralları

- TC Kimlik numaraları 11 basamaktan oluşmaktadır. İlk 9 basamak arasında kurulan bir algoritma
 bize 10. basmağı, ilk 10 basamak arasında kurulan algoritma ise bize 11. basamağı verir.

- 11 hanelidir.

- Her hanesi rakamsal değer içerir.

- İlk hane 0 olamaz.

- 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı 
    çıkartıldığında, elde edilen sonucun 10′a bölümünden kalan, yani Mod10′u bize 10. haneyi verir.

- 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10′a 
    bölümünden kalan, yani Mod10′u bize 11. haneyi verir.

"""

