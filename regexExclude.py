import re

regex_pattern = r'[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.\,]'

print(str(bool(re.search(regex_pattern, input('type in a string:\n')))).lower())