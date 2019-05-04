import re

regex_pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'

print(str(bool(re.search(regex_pattern, input()))).lower())
