def group_by_owners(files):
    return None

files = {
    'Input.txt' : 'Randy',
    'Code.py' : 'Stan',
    'Output.txt' : 'Randy'
    }

# print(group_by_owners(files))

owners = {}

for k,v in files.items():
    if v not in owners:
        owners[v] = [k]
    elif v in owners:
        owners[v].append(k)
print(owners)