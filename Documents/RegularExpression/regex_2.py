import re 
# sets 
""" 
[abc] : a,b,c
[^abc] : not a,b,c
[a-z] : a to z
[^a-z] : not a to z
[A-Z] : A to Z
[^A-Z] : not A to Z
[a-zA-Z] : a to z or A to Z
[^a-zA-Z] : not a to z or A to Z
[0-9] : 0 to 9
[^0-9] : not 0 to 9
[0-9a-zA-Z] : 0 to 9 or a to z or A to Z
[^0-9a-zA-Z] : not 0 to 9 or a to z or A to Z
"""
test_string = """ Patika Dev 153- Yemek Sepeti Yemeksepeti yemeksepeti Patika dev patikadev -dev"""
# print(r"[PY]",*re.finditer(r"[PY]", test_string),sep="\n")
# print(r"[^PY]",*re.finditer(r"[^PY]", test_string),sep="\n")
# print(r"[a-z]",*re.finditer(r"[a-z]", test_string),sep="\n")
# print(r"[^a-z]",*re.finditer(r"[^a-z]", test_string),sep="\n")
# print(r"[A-Z]",*re.finditer(r"[A-Z]", test_string),sep="\n")
# print(r"[^A-Z]",*re.finditer(r"[^A-Z]", test_string),sep="\n")
# print(r"[a-zA-Z]",*re.finditer(r"[a-zA-Z]", test_string),sep="\n")
# print(r"[^a-zA-Z]",*re.finditer(r"[^a-zA-Z]", test_string),sep="\n")
# print(r"[0-9]",*re.finditer(r"[0-9]", test_string),sep="\n")
# print(r"[^0-9]",*re.finditer(r"[^0-9]", test_string),sep="\n")
# print(r"[0-9][0-9][0-9]",*re.finditer(r"[0-9][0-9][0-9]", test_string),sep="\n")
# print(r"[0-9a-zA-Z]",*re.finditer(r"[0-9a-zA-Z]", test_string),sep="\n")
### Quantifiers
"""
* : zero or more
+ : one or more
? : zero or one
{n} : exactly n
{n,} : n or more
{n,m} : n to m
"""
test_string = "merhaba_123_456_merhaba_7 89182222 789 12312"
# print(r"\d*",*re.finditer(r"\d*", test_string),sep="\n")
# print(r"\d+",*re.finditer(r"\d+", test_string),sep="\n")
# print(r"_?\d",*re.finditer(r"_?\d", test_string),sep="\n")
# print(r"\d{3}",*re.finditer(r"\d{3}", test_string),sep="\n")
# print(r"\d{3,}",*re.finditer(r"\d{3,}", test_string),sep="\n")
# print(r"\d{3,5}",*re.finditer(r"\d{3,5}", test_string),sep="\n")

#### dates 
tarihler = """
12/12/12
12/04/2012
12/08/2012 12:12
2012/05/12 12:12
2022/07/12

12-12-12
12-12-2012
12-12-2012 12:12
2012-12-12 12:12
2022-12-12
08-18-2012
08-18-2012 12:12
08-18-2012 12:12:12
08-18-2012 12:12:12.123

12.12.12
12.12.2012
12.12.2012 12:12
2012.12.12 12:12
2022.12.12


"""

# pattern = re.compile(r"\d\d\d\d-\d\d-\d\d")
# print(pattern.findall(tarihler))
# pattern = re.compile(r"\d\d\d\d[-/\.]\d\d[-/\.]\d\d")
# print(pattern.findall(tarihler))
# pattern = re.compile(r"\d{4}[-/\.]0[5-7][-/\.]\d{2}")
# print(pattern.findall(tarihler))
# pattern = re.compile(r"\d{4}[-/\.]\d{2}[-/\.]\d{2}")

# pattern = re.compile(r"(\d{4})[-/\.](\d{2})[-/\.](\d{2})")
# matches = pattern.finditer(tarihler)
# for match in matches:
#     print(match.group(0),match.group(1),match.group(2),match.group(3))
#     print(match.groups())


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
# epostalar = """
# buks.2180@816qs.com
# abRaHam_sw33tv0ice@agirdagi.t3y
# ali.man77_@eposta.co.uk
# """
# pattern = re.compile(r"([a-zA-Z0-9-._]+)@([a-zA-Z0-9-]+)\.([a-zA-Z0-9-._]+)")
# ### sub split
# matches = pattern.finditer(epostalar)
# for match in matches:
#     print(match.groups())





# test_string = """ Patika Dev 153- Yemek Sepeti Yemeksepeti yemeksepeti yemeksepeti Patika dev patikadev -dev"""
# pattern = re.compile(r"yemeksepeti")
# subbed = pattern.sub("YEMEKSEPETİ",test_string)
# print(subbed) # Patika Dev 153- Yemek Sepeti Yemeksepeti YEMEKSEPETİ YEMEKSEPETİ Patika dev patikadev -dev


test_string = """
http://www.yemeksepeti.com
https://www.patika.dev
http://kodluyoruz.com
"""

# pattern = re.compile(r"https?://(www.)?([a-z]+)\.([a-z]+)")
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match.groups())
#     print(match.group(2))
#     print(match.group(3))

# subbed_url = pattern.sub(r"\2.\3",test_string)
# print(subbed_url)


metin = "Jamiryo JAMIRYO"
pattern = re.compile(r"jamiryo",re.I) # or re.IGNORCASE
print(*pattern.finditer(metin),sep="\n")




