import sys

n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(input()))

# sansul calc
def sansul(list,n):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    final = round(sum / n)
    if final == -0:
        final = 0
    return final
print(sansul(list,n))

# middle value
def middle_val(list):
    list.sort()
    mid = len(list)//2

    return list[mid]
print(middle_val(list))

# most exist I have to think about negative numbers
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
    if len(map) <= 2:
        return map[0]
    else:
        return map[1]
print(most_val(list))

#range
def range_val(list):
    check = min(list)
    if len(list) == 1:
        return 0
    else:
        if check < 0:
            check *= -1
        return max(list) + check
print(range_val(list))
