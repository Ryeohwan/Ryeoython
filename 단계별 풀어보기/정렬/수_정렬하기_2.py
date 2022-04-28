import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(input()))

# # use sort
# list.sort()
# for i in range(len(list)):
#     print(list[i])

# I do not know what is difference
# this make loading

# insert sort rough
def insert_sort(list):
    for i in range(len(list)):
        for j in range(i,0,-1): # from i to 0 go -1
            if list[j -1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
                # do not need new variable

# insert sort refactoring
def insert_sort(list):
    for i in range(1,len(list)):
        while i > 0 & list[i - 1]> list[i]:
            list[i - 1], list[i] = list[i], list[i-1]
            i -= 1


# selection sort
def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
# checking i each j

# bubble sort
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        swapped = False
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break

# I have to study heap and quick