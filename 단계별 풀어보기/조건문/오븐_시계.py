import sys
from unittest import case

a, b = map(int, input().split(' '))
if a in range(0,26) and b in range(0,60):
    time = int(input())
    if time in range(0,1001):
        min = b + time
        if time >= 60:
            if time % 60 == 0:
                time == 00
                a += 1
                if a >= 24:
                    a = 0
                    print(a,min)
                else:
                    print(a, min)
            elif time // 60 > 1:
                time -= 60
                a += time // 60
                print(a,min)
        else:
            print(a,min)
else:
    print('You entered wrong time range')