import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(sys.stdin.readline())

list.sort()
new_list = ''.join(list)
final = new_list[:-1]
print(final)