import sys

n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(input())

# sansul
def sansul(list,n):
    for i in range(len(list)):
        sum += list[i]
    return sum // n
print(sansul(list,n))