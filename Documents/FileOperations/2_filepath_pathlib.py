from pathlib import Path
print(Path("Documents","FileOperations"))
liste = ["ali.py","veli.py"]
for item in liste:
    print(Path("Documents","FileOperations",item))
#######################
sonuc  = Path("Documents") / "FileOperations" / "deneme.py"
print(sonuc.is_absolute())
print(sonuc)
print(Path.cwd())

print(sonuc)
print(sonuc.exists())
print(sonuc.is_file())
print(sonuc.is_dir())
print(sonuc.is_absolute())
print(sonuc.name) #deneme.py
print(sonuc.stem) #deneme
print(sonuc.suffix) #.py
print(sonuc.parent) #Documents\FileOperations
print(*sonuc.parents) #[Path('Documents'), Path('FileOperations')]
adres = Path.cwd() /"Documents" / "Functions"
print(*adres.glob("*.py"),sep="\n")