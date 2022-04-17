import sys

n = int(sys.stdin.readline())
star = []
add = '*'

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
        add = ''.join(star)
    result = ''.join(star)
    print(result)
make_star(n,star,add)
# In the middle, They got all \n and ' '
# I'll use count for \n

# 한글로 적어둬야겠다. 
# 내 생각은 그렇다.
# 먼저 그러니까 입력값 3짜리 별을 미리 만들어둔다.
# 그리고 n값이 3보다 크다면 재귀를 통해서 
# add라는 것에 join 연산으로 집어넣어서 합쳐주려고 
# 한다.
