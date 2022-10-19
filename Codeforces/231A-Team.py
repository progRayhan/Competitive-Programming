n = int(input())
total = 0

for i in range(n):
    a = str(input())
    b = a.count("1")
    if b>=2:
        total += 1

print(total)