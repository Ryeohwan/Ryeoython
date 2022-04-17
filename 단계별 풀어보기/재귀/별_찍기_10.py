import sys

n = int(sys.stdin.readline())
star = ''
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

# make_star(count,star,check,add,blank)
# I have to use ['***', '* *', '***']
def make_star(n,star):
    for _ in range(n*n):
        star += '*'
    print(star)
    
make_star(n,star)

