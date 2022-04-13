import sys
a = int(sys.stdin.readline())

# a_list = [[f'{j+1}/{i+1}' for i in range(a)] for j in range(a)]
# 너무 비효율적이다.

line_sum = 1
line = 1 # 과 그 줄의 최대값과 동일하다.
while a > line_sum:
    line += 1
    line_sum += line
dist = a - line_sum + line


if line % 2 != 0:
    top = line - dist + 1 
    bottom = dist
else:
    top = dist
    bottom = line - dist + 1

print(f'{top}/{bottom}')