def non_self():
    self_list=[]
    sum = 0
    for i in range(1,10001):  # 만약 n억개의 수를 원한다면 조정해주면 된다.
            for j in range(len(str(i))):
                sum += int(str(i)[j]) # 자릿수의 합을 위함
            sum += i # 자기 자신도 더해줘야 한다.
            self_list.append(sum)
            sum = 0 # 초기화를 시켜줘야 누적합이 되지 않는다.
    return sorted(self_list)

def find_self(non_self):
    result = []
    for i in range(1,10001): # n억 개의 수를 원한다면 조정해주면 된다.
        if i not in non_self:
            result.append(i)
    return result

for i in find_self(non_self()): # 출력 형식을 맞추기 위함
    print(i) 