# import re

# test_string = "123abc456789abc123ABC"
# #              0123456
# pattern = re.compile(r"abc")
# # MATCH METHOD
# #### finditer
# matches = pattern.finditer(test_string)
# print(matches) #<callable_iterator object at 0x0000029EF7407D60>
# for match in matches:
#     print(match)
# #  <re.Match object; span=(3, 6), match='abc'>
# #  <re.Match object; span=(12, 15), match='abc'>
# #### findall()
# # matches = pattern.findall(test_string)
# # print(matches) #['abc', 'abc']
# # for match in matches:
# #     print(match)
# #### search()
# match = pattern.search(test_string) # bulduğu ilk elemanı match olarak döndürür
# print(match) # <re.Match object; span=(3, 6), match='abc'>
# #### match()
# test_string = "123abc456789abc123ABC"
# match = pattern.match(test_string) # ilk elemanın başına match olup olmadığını kontrol eder
# print(match) # None
# test_string = "abc123abc456789abc123ABC"
# match = pattern.match(test_string) # ilk elemanın başına match olup olmadığını kontrol eder
# print(match) # <re.Match object; span=(0, 3), match='abc'>

### GROUP METHOD
# test_string = "123abc456789abc123ABC"
# pattern = re.compile(r"abc")
# ### group start end span
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)
#     print(match.group()) #abc
#     print(match.start()) #3
#     print(match.end()) #6
#     print(match.span()) #(3, 6)

# META CHARACTERS
meta = " . ^ $ * + ? { } [ ] \ | ( )"
""" 
. : any character except newline
^ : start of string or line (beginning of line)
$ : end of string or line (if not at end of string) 
* : zero or more occurrences of preceding re
+ : one or more occurrences of preceding re
? : zero or one occurrence of preceding re
{m} : exactly m occurrences (n is a positive integer)
{m,} : m or  more occurrences (n is a positive integer)
{m,n} : m to n occurrences (n is a positive integer)
[] : character set (list of characters) - [abc] = a,b,c (a,b,c) [^abc] = not a,b,c (not a,b,c) [a-z] = a to z (a to z) [^a-z] = not a to z (not a to z)
####################
\d : digit (0-9)
\D : not a digit (0-9)
\w : word character (a-z, A-Z, 0-9, _)
\W : not a word character (a-z, A-Z, 0-9, _)
\b : word boundary (\w or \W)
\B : not a word boundary (\w or \W)
\s : whitespace (space, tab, newline)
\S : not whitespace (space, tab, newline)
\A : start of string
\Z : end of string
\z : end of string (if not at end of string)
\ : escape character
| : or (abc|def) = abc or def
() : group 

ASCII, A: Make several characters into a single character \w \b \s \d match only ASCII characters
DOTALL, S: Make . match any character including newline
IGNORECASE, I: Ignore case when matching
LOCALE, L: Ignore case when matching
MULTILINE, M: Make ^ and $ match the beginning and end of any line (not just the beginning and end of the string)
VERBOSE, X: Ignore whitespace and comments in the pattern
"""

# pattern = re.compile(r"abc", re.ASCII)
# matches = pattern.finditer(test_string)
# re.finditer(r"abc", test_string)
# test_string = "123abcab456789abc123ABCab"
# print(r".",*re.finditer(r".", test_string),sep="\n")
# print(r"^",*re.finditer(r"^123", test_string),sep="\n")
# print(r"$",*re.finditer(r"ABC$", test_string),sep="\n")
# print(r"*",*re.finditer(r"abc*", test_string),sep="\n")
# print(r"+",*re.finditer(r"abc+", test_string),sep="\n")

test_string = """ Patika Dev 153- Yemek Sepeti Yemeksepeti yemeksepeti 
Patika dev patikadev -dev"""
# print(r"\d",*re.finditer(r"\d", test_string),sep="\n")
# print(r"\D",*re.finditer(r"\D", test_string),sep="\n")
# print(r"\w",*re.finditer(r"\w", test_string),sep="\n")
# print(r"\W",*re.finditer(r"\W", test_string),sep="\n")
# test_string = "dev patikadev -dev"
# print(r"\b",*re.finditer(r"\bdev", test_string),sep="\n")
# print(r"\B",*re.finditer(r"\Bdev", test_string),sep="\n")
# print(r"\s",*re.finditer(r"\s", test_string),sep="\n")
# print(r"\S",*re.finditer(r"\S", test_string),sep="\n")

