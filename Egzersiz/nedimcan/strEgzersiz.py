#var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın 
#Yukarıdaki çıktıyı almak için gereken python kodunu yazınız. 

var1 = "Teşekkürler Süpermen"

#Solution1 -> Baran
#print(var1[::-1].replace('e', 'i', 2)[::-1])

#Solution2
# var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın
# var2 = var1.split()
# var2 => ["Teşekkürler","Süpermen"]
# var2[1]  = var2[1].replace("e","ı")
# var1 = " ".join(var2)
# print(var1)