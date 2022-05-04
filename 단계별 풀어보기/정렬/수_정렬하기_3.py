import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(input()))

#Let's study heap quik merge

# merge sort
def merge_sort(list):
    if len(list) < 2:
        return list
    mid = len(list)//2 
    low_list = merge_sort(list[:mid])
    high_list = merge_sort(list[mid:])
    merged_list = []

    l= h= 0

    while l < len(low_list) and h < len(high_list):
        if low_list[l] < high_list[h]:
            merged_list.append(low_list[l])
            l += 1
        else:
            merged_list.append(high_list[h])
            h += 1
    merged_list += low_list[l:]
    merged_list += high_list[h:]
    return merged_list

# final = merge_sort(list)
# for i in range(len(final)):
#     print(final[i])

# quik sort
def quick_sort(list):
	if len(list) <= 1:
		return list
	pivot = len(list) // 2
	front_list, pivot_list, back_list = [], [], []
	for value in list:
		if value < list[pivot]:
			front_list.append(value)
		elif value > list[pivot]:
			back_list.append(value)
		else:
			pivot_list.append(value)
	return quick_sort(front_list) + quick_sort(pivot_list) + quick_sort(back_list)


# final = quick_sort(list)
# for i in range(len(final)):
#     print(final[i])