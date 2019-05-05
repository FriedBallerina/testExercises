import re

regex_pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

print(str(bool(re.search(regex_pattern, input()))).lower())

