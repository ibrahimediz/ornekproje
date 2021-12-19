mySet = set()

mySet.add(input("Enter the first one: "))
mySet.add(input("Enter the second one: "))

if len(mySet) == 1:
    if mySet[0] == 45:
        print("İkizkenar")
    elif mySet[0] == 60:
        print("Eşkenar")
else:
    if mySet[0] == 90 or mySet[1] == 90:
        print("Diküçgen")
    else:
        print("Çeşitkenar")

        

