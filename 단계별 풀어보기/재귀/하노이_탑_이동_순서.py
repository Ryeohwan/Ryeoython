import sys

# number of plate
n = int(sys.stdin.readline())

def hanoi(n, start, middle, end):  
    # It's the rule of hanoi's last move
    if n == 1:
        print(start, end)
    else:
        # it's the main of hanoi
        hanoi(n-1,start,end,middle) 
        print(start, end)
        hanoi(n -1, middle, start, end)

print(2**n -1)
hanoi(n, 1, 2, 3)


