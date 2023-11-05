N = int(input())
for i in range(1, N+2):
    if i % 2 == 0:
        i *= (-1)
    if abs(i) == N+1:
        print(i)
        