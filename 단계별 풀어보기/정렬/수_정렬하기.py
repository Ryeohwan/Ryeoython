import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(input()))
    # I have to change type str to int

list.sort()
for i in range(len(list)):
    print(list[i])