import re

regex_pattern = r'^\d{2,}[a-z]*[A-Z]*$'

print(str(bool(re.search(regex_pattern, input()))).lower())