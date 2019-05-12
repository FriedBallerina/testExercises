import re

regexLookahead = re.compile(r'o(?=o{2})')

searchResult = re.findall(regexLookahead, 'gooooo!')
print(searchResult)
