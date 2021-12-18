"""
var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın 
Yukarıdaki çıktıyı almak için gereken python kodunu yazınız. 
"""
# handy
var1 = "Teşekkürler Süpermen"
print(var1[::-1].replace('e', 'i',2)[::-1])

# second way
var1 = "Teşekkürler Süpermen"
var2 = var1.replace("Süpermen",var1.split()[1].replace("e", "ı"))