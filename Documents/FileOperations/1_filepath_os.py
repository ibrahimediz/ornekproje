"""
Abs Path  /workspace/ornekproje/Documents/FileOperations/1_filepath.py
Relative Path Documents/FileOperations/1_filepath.py
"""
import os
# print(os.sep)
# print(os.getcwd())
# liste = [os.getcwd(),"Documents","FileOperations"]
# print(os.sep.join(liste)) #1 /workspace/ornekproje/Documents/FileOperations
# os.path.join(os.getcwd(),"Documents","FileOperations") #2 /workspace/ornekproje/Documents/FileOperations
# print(os.path.exists(os.path.join(os.getcwd(),"Documents","FileOperations","1_filepath.py")))
# print(os.walk("/workspace/ornekproje"))
# for adres,klasor,dosya in os.walk("/workspace/ornekproje"):
#     print(f"Adres:{adres}")
#     print(f"Klasör:{klasor}")
#     print(f"Dosya:{dosya}")
# os.chdir(".")
# print(os.getcwd()) # /workspace
from pathlib import Path
import os
import datetime as dt 
tarih = dt.datetime.now()
os.makedirs(Path(str(tarih.year),str(tarih.month),str(tarih.day),str(tarih.hour+3)))
