import re

regexNegativeLookahead = re.compile(r'(.)(?!\1)')

searchResult = re.findall(regexNegativeLookahead, '###$$$$') # '###$$$$')
print(searchResult)