"""Str"""
"""
    var = '' differs from var = ""
                          ex: var = 'Ankara'da' syntax error
                          ex: var = "Ankara'da" compiles
    
    Triples quotes allow multiple lines
"""

var1 ="Yemeksepeti"  # index starts from 0 also works reverse ex below
print(var1[10]) # i
print(var1[-1]) # i
print(var1[0:5]) # Yemek 0 1 2 3 4, 5 wont be included
print(var1[:5]) # Yemek 0 1 2 3 4, 5 wont be included   starting point is not needed
print(var1[:-6]) # Yemek 0 1 2 3 4, 5 Starts from 0 to index -6 and -6 not included (s)
print(var1[5:11]) # Sepeti 5 6 7 8 9 10
print(var1[5:]) # Sepeti 5 6 7 8 9 10 end point is not needed
print(var1[1::2]) # eespt  starts from 1 to the end with 2 steps
"""
    [start:end:step]
"""

var2 = "Teşekkürler Süpermen"
print(var2.replace("e", "ı").replace("ü", "ı"))

# # var2 => ["Teşekkürler","Süpermen"]
# var2[1]  = var2[1].replace("e","ı")
# var1 = " ".join(var2)
# print(var1)