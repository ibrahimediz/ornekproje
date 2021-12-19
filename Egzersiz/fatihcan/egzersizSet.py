uniq_list = {}
text = input('metin giriniz')
count = 0

for x in text:
    if x not in uniq_list:
        count +=1
        uniq_list.append(x)
print(uniq_list)