a, b, c = map(int, input().split(' '))

list = [a,b,c]

list.sort()
check = 0
flag = 0
for i in range(len(list)):
    if list[1] == list[i]:
        check += 1
        flag = list[i]

if check == 3:
    print(10000 + flag*1000)
elif check == 2:
    print(1000 + flag*100)
else:
    print(list[-1]*100)