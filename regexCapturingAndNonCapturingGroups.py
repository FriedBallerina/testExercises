import re

regexPattern = re.compile(r'(ok){3,}')

print(bool(re.search(regexPattern, input())))