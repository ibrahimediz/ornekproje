print(0x6D) # 2 => 109
print(bin(0x6D)) # 0b1111110
print(str(bin(0x6D))[2:]) # 1111110
print(str(bin(0x6D))[2:].zfill(7)) # 1111110
a,b,c,d,e,f,g = map(int,list(str(bin(0x6D))[2:].zfill(7)))
print(a,b,c,d,e,f,g)
print(("*" if a else " ")*8)
print("*" if f else " "," "*4,"*" if b else " ")
print("*" if f else " "," "*4,"*" if b else " ")
print(("*" if g else " ")*8)
print("*" if e else " "," "*4,"*" if c else " ")
print("*" if e else " "," "*4,"*" if c else " ")
print(("*" if d else " ")*8)
#####################################
import math 

column = 3    
row = 5 
sevenSegment=[]
emptyRow = [" "] * column


for i in range(row):
    sevenSegment.append(emptyRow.copy())

def fillA():
    for i in range(row):
        for j in range(column):
            sevenSegment[i][j] = "*"
        break

def fillB():
    for i in range(math.ceil(row/2)):
        for j in range(column):
            if j==column-1:
                sevenSegment[i][j] = "*"

def fillC():
    for i in range(math.floor(row/2),row):
        for j in range(column):
            if j==column-1:
                sevenSegment[i][j] = "*"

def fillD():
    for i in range(row-1,row):
        for j in range(column):
            sevenSegment[i][j] = "*"
        
def fillE():
    for i in range(math.floor(row/2),row):
        for j in range(column):
            if j==0:
                sevenSegment[i][j] = "*"
    
def fillF():
    for i in range(math.ceil(row/2)):
        for j in range(column):
            if j==0:
                sevenSegment[i][j] = "*"

def fillG():
    for i in range(math.floor(row/2),math.floor(row/2)+1):
        for j in range(column):
            sevenSegment[i][j] = "*"


# Yukaridaki kodlar icin Ilhan' a tesekkur ederim. :D

funcList = [fillA, fillB, fillC, fillD, fillE, fillF, fillG]

def getNumber():
    number = int(input('enter number:'))

    numberMatch = {
        0: '1111110',
        1: '0110000',
        2: '1101101',
        3: '1111001',
        4: '0110011',
        5: '1011011',
        6: '1011111',
        7: '1110000',
        8: '1111111',
        9: '1111011'
    }

    return numberMatch[number]


def printsevenSegment():

    number = getNumber()

    for index, value in enumerate(number):
        if int(value):
            funcList[index]()

    for i in range(row):
        for j in range(column):
            print(sevenSegment[i][j],end=" ")
            if(j==column-1):
                print("\n")
                
printsevenSegment()