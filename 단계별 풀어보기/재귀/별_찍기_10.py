import sys

n = int(sys.stdin.readline())
star = []
star_dust = ['***', '* *', '***']
add = '*'
# count = n // 3
# check = 0
# add = '*'
# blank = ' '
# def make_star(count,star,check,add,blank):
#     for i in range(9):
#         if i == 4:
#             star += blank
#         elif i == 3 or i == 6:
#             star += '\n'
#             star += add
#         else:
#             star += add
#     print(f'star:\n{star}')
#     print(f'add:\n{add}')
#     print(f'blank:\n{blank}')
#     add = star
#     blank = ' ' * len(add)
#     check += 1
#     if check == count:
#         print(f'final:\n{star}')
#     else:
#         make_star(count,star,check,add,blank)

# 012 3 5 678 012345678 9 11

# make_star(count,star,check,add,blank)
# I have to use ['***', '* *', '***']
def make_star(n,star,add):
    count = 0
    for _ in range(n*n):
        count += 1
        if count % n == 0:
            if count != n*n:
                star.append(f'{add}\n')
            else:
                star.append(add)
        else: # I have to make blank in this else
            star.append(add)
    result = ''.join(star)
    print(result)
make_star(n,star,add)
# In the middle, They got all \n and ' '
# I'll use count for \n

