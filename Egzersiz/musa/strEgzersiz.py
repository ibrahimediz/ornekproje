var1 = "Teşekkürler Süpermen"

# Cevap
# print(var1[::-1].replace("e", "i", 2)[::-1])

var2 = var1.split()
var2[1] = var2[1].replace("e", "ı")
var1 = " ".join(var2)
print(var1)