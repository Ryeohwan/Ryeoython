import sys
a = int(sys.stdin.readline())
final = 1

# def non_recur(a):
#     final = 1
#     for i in range(1, a+1):
#         final *= i
#     return final

def recur(a,final):
    if a == 0:
        print(1)
    else:
        final *= a
        a -= 1
        if a == 1:
            print(final) 
        else:
            recur(a,final)


recur(a,final)