liste = ["ilhanmert","canersoy","efecan",
"mustafaismail","ayseberna","enes",
"hasan","ege","nedimcan","ahmetbaran",
"fahrettinorkun","celalbugra","onur","musa",
"alibaris","ardacem","irem","seyit","bilal",
"abdullahekrem","ali","furkan","fatihcan"]
import os

folderName = "Odevler"
# os.mkdir(folderName)
fileName = "ilk"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    open(os.path.join(folderName,item,f"{fileName}.py"),"w")