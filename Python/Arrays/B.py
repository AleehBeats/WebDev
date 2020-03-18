a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
for i in range(a):
    if b[i]%2==0:
        print(b[i])