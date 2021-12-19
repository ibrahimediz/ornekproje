"""
iki açısı girilmiş olan bir üçgenin açılara göre türünü ekrana yazdıran python programını yazınız
45,45  45,90  1. İkizKenar Üçgen Dik Üçgen
60,60         2. Eşkenar Üçgen
90,25         3. Dik üçgen
120,41        4. Çeşit Kenar
"""

def get_triangle_type(angle_1=45, angle_2=45):
    triagnle_set = set(angle_1, angle_2)
    triangle_type = ""
    if len(triagnle_set) == 1:
        pass


def return_dictionary(text):
    char_set = set(text)
    char_dict = {}
    for char in char_set:
        char_dict[char] = 0
    
    for char in text:
        char_dict[char] += 1
    
    return char_dict

print(return_dictionary("yemeksepeti"))