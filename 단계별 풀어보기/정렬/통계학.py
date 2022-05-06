import sys

n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(input()))

# sansul
def sansul(list,n):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum // n
print(sansul(list,n))

# middle value
def middle_val(list,n):
    list.sort()
    mid = len(list)//2
    return list[mid]

# most exist
def most_val(list):
    index_list = [0] * 500001
    for i in range(len(list)):
            index_list[list[i]] += 1
    new_list = []
    for index,value in enumerate(index_list):
        if value > 0:
            new_list.append([index,value])
    check = new_list[0][1]
    map = []
    for i in range(len(new_list)):
        if new_list[i][1] > check:
            check = new_list[i][1]
    for i in range(len(new_list)):
        if new_list[i][1] == check:
            map.append(new_list[i][0])
    map.sort()
    return map[-2]

print(most_val(list))
