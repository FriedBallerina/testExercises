import re

regexPattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$')

print(bool(re.search(regexPattern, input())))