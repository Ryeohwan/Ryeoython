import sys

n = int(sys.stdin.readline())
stars = ['***','* *','***']
# 012 3 5 678 012345678 9 11

# make_star(count,star,check,add,blank)
# I have to use ['***', '* *', '***']
# def make_star(n,star,ways):
#     count = 0
#     for _ in range(n):
        
# if n == 3:
#     print(three)
# else:
#     make_star(n,star,ways)

# 한글로 적어둬야겠다. 
# 내 생각은 그렇다.
# 먼저 그러니까 입력값 3짜리 별을 미리 만들어둔다.
# 그리고 n값이 3보다 크다면 재귀를 통해서 
# add라는 것에 join 연산으로 집어넣어서 합쳐준다.
# 그냥 2차원 배열을 사용해보아도 된다.

# recursion
# def make_star(n,star):
# # When -> after def is describe return value
#     add = []
#     if n == 3:
#         return star
#     else:
#         for i in star:
#             add.append(i*3) # 무조건 3배씩 늘어나게 되는구나
#         for i in star: # 각 줄당 for 문을 이용하여 따로 개행을 쓰지 않아도 됨
#             add.append(i + ' ' * len(star) + i)
#         for i in star:
#             add.append(i * 3)
#         return make_star(n//3, add)

# final = make_star(n,star)
# for i in final:
#     print(i)

# no recursion

# star = ['*' for _ in range(n*n)]
# count = 0
# for i in range(len(star)): # fill stars 
#     if i != 0:
#         if  i % n == 0:
#             star[i] = '\n*'
# for i in range(len(star)):
#     print('I can not solve this algo')
# result = ''.join(star)
# print(result)

# 0, 2, 6, 8 full stars
# 1, 7 * ** ** ** * shape


count = 0
while n > 3:
    n //= 3
    count += 1
# n //= 3 n 에 3으로 나눈 몫을 저장해라

# # fill stars
# def make_star():
#     star = len(stars)
#     newstars = []
#     for i in range(star*3):
#         newstars.append(stars[i % star]*3)
#     return newstars


# insert blank
def make_star():
    star = len(stars)
    newstars = []
    for i in range(star*3):
        if i // star == 1:
            newstars.append(stars[i % star] + ' ' * star + stars[i % star])
        else:
            newstars.append(stars[i % star]*3)
    return newstars

for i in range(count):
    stars = make_star()

for i in stars:
    print(i)