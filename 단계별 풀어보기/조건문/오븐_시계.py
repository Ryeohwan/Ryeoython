a, b = map(int, input().split(' '))
if a in range(0,26) and b in range(0,60):
    time = int(input())
    if time in range(0,1001):
        min = b + time
        add_hour = min // 60
        if add_hour == 0:
            print(a,min)
        else:
            hour = a + add_hour
            minute = min % 60
            if hour > 24:
                hour -= 24
                print(hour,minute)
            elif hour == 24:
                hour = 0
                print(hour,minute)
            else:
                print(hour,minute)
else:
    print('You entered wrong time range')