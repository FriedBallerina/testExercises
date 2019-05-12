import re

regexTagPattern = re.compile(r'<\w*[>| ]')
numberOfStrings = int(input())
tags = []

def FindTags():
    
    inputText = input()   
    tag = re.findall(regexTagPattern, inputText)
    
    for j in tag:
        j = j.strip('<> ')
        if j not in tags:
            tags.append(j)
    
    tags.sort()
            
for i in range(numberOfStrings):
    FindTags()
    
for k in tags:
        if tags.index(k) != len(tags)-1:
            print(k + ';', end = '')
        else:
            print(k)