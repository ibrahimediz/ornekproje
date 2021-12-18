# Tek tırnak veya çift tırnak aynı şeyi yapar. Ancak noktlama işaretlerini kullanmak için her ikisini de kullanmamız gerekir

print("Neler neler yapıyorsun bensizken Ankara'da?")

# Üç tırnak ise fazla satırlı tanımlamalar için kullanılabilir.

print("""Neler neler yapıyorsun
bensizken Ankara'da?""")
################################
var1 = "YemekSepeti"
# İndisler 0'dan başlar, -e kadar devam eder.
print(var1[0]) => "Y"

# (-) işareti ile sondan da başlayabilirsin.
print(var1[-10]) => "t"

# İndisler arasında (:) kullanarak istediğimiz karakterleri alabiliriz.
print(var1[0:5]) => "Yemek"

# İndis başlangıcını belirtmezsek eğer 0. elemandan başlar.
print(var1[:5]) => "Yemek"

# İndis bitişini belirtmezsek 5. elemandan sonuncu elemana kadar yazar.
print(var1[5:]) => "Sepeti"

# İndis bitişini aynı şekilde tersten de yapabiliriz.
print(var1[:-6])

var2 = "Yaşamak"

# 1'den başla, 2 adım atlayarak devam et.
print(var2[1::2]) => "aaa"

# 0'dan başla, 2 adım atlayarak devam et.
print(var2[::2]) => "Yşmk"

var3 = "Teşekkürler Süpermen"
var3.replace("S", "T") # S harfini T ile değiştirir
var3.replace("e", "ı").replace("ü", "ı")
var3.replace(old, new, 3)

