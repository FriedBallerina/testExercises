import re

regex_pattern = r'[a-zA-Z]*s$'

print(str(bool(re.search(regex_pattern, input()))).lower())