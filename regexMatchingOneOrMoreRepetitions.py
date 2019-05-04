import re

regex_pattern = r'^\d+[A-Z]+[a-z]+$'

print(str(bool(re.search(regex_pattern, input()))).lower())
