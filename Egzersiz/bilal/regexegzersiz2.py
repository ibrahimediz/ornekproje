
isimler = """
Merhaba
123123123123
2022-12-12
Mr. Simit
Mr. Kızılay
Mr. Kahverengi
Mr. Lacivert
Ms. Kırmızı
Ms. Yeşil
Mrs. Siyah
Mrs. Mavi
edizibrahim@patika.dev
patika@kodluyoruz.com
"""

##isimleri ayıklama
# pattern = re.compile(r"(Mr|Mrs|Ms).?\s(\w+)")
# matches = pattern.finditer(isimler)
# for match in matches:
#     print(match.group(2))
# patika@kodluyoruz.com
import re
pattern = re.compile(r"(.*)+@+(.*)")
matches = pattern.finditer(isimler)
for match in matches:
    print(match)
