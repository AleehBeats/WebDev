a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
for i in range(a):
    if i%2==0:
        print(int(b[i]))