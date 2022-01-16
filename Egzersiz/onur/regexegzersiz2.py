import re

isimler = """
edizibrahim@patika.dev
patika@kodluyoruz.com
"""


pattern = re.compile(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")
matches = pattern.finditer(isimler)
for match in matches:
    print(match.groups())