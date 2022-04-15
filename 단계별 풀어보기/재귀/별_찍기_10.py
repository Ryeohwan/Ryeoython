import sys

n = int(sys.stdin.readline())
star = ''
count = n // 3
check = 0
add = '*'
def make_star(count,star,check,add):
    for i in range(9):
        if i == 4:
            star += ' '
        elif i == 3 or i == 6:
            star += '\n'
            star += add
        else:
            star += add
    print(f'star:\n{star}')
    print(f'add:\n{add}')
    add = star
    check += 1
    if check == count:
        print(f'final:\n{star}')
    else:
        make_star(count,star,check,add)

make_star(count,star,check,add)