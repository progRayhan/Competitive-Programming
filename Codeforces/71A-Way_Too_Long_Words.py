n = int(input())
for i in range(n):
    a = str(input())
    if len(a) > 10:
        print(a[0]+str(len(a[1:-1]))+a[-1])
    else:
        print(a)