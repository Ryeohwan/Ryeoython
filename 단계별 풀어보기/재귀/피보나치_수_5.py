import sys
n = int(sys.stdin.readline())
fibo = [0,1,1]

# non_recur
# def make_fibo(n,fibo):
#     if n > 2:
#         for i in range(2,n+1):
#             fibo[i] = fibo[i -2] + fibo[i - 1]
#             fibo.append(fibo[i])
#         fibo.pop()
#     else:
#         return fibo[n]

def make_fibo(n,fibo):
    if n > 0:
        n -= 1
        sum = fibo[-1] + fibo[-2]
        fibo.append(sum)
        make_fibo(n,fibo)
    else:
        return fibo[n]
    


make_fibo(n,fibo)
print(fibo[n])