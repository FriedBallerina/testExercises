import re

match = 'hackerrank'

for i in range(int(input())):
    newInput = input()
    if newInput.startswith(match) and newInput.endswith(match):
        print(0)
    elif newInput.endswith(match):
        print(2)
    elif newInput.startswith(match):
        print(1)
    else:
        print(-1)