import sys
n = int(sys.stdin.readline())


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

# for i in range(len(quick_sort(list))):
#     print(quick_sort(list)[i])

# for use lower memory
check_list = [0] * 10001

for i in range(n):
    input_num = int(sys.stdin.readline())
    check_list[input_num] += 1  # 10001 범위의 입력받은 값을 인덱스에다가

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)