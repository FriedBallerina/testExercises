import re

regexBackreference = re.compile(r'\d{2}(-?)(\d\d\1){2}\d\d')

searchResult = re.search(regexBackreference, '12-34-56-78')
print(searchResult.group())