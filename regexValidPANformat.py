import re

regex_pattern = r'^[A-Z]{5}\d{4}[A-Z]$'
enteredValue = input()
#example input: '''3
#ABCDS1234Y
#ABAB12345Y
#avCDS1234Y'''

values = enteredValue.split('\n')
numberOfLines = values[0]
possiblyPanNumbers = values[1:]

for i in possiblyPanNumbers:
    if bool(re.search(regex_pattern, i)) == False:
        print('NO')
    else:
        print('YES')