s1 = input().lower()
s2 = input().lower()

if (len(s1)<=100 and len(s2)<=100):
    if (s1<s2):
        print(-1)
    elif (s2<s1):
        print(1)
    elif (s2==s1):
        print(0)