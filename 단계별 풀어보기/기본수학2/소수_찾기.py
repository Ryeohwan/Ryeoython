import sys

n = int(sys.stdin.readline())
n_list = list(map(int,input().split(' ')))
prime_check = 0
if len(n_list) != n:
    print('You entered wrong numbs')
else:
    for i in n_list:
        check = 0
        if i > 1:
            for j in range(2,i):
                if i % j ==0:
                    check += 1
            if check == 0:
                prime_check += 1
print(prime_check)