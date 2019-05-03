#!/bin/python3

N = int(input())
weird = 'Weird'
not_weird = 'Not Weird'

if N%2 == 1:
    print(weird)
elif N%2 == 0:
    if N >= 2 and N <= 5:
        print(not_weird)
    elif N >= 6 and N <= 20:
        print(weird)
    else:
        print(not_weird)