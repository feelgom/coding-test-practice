N=int(input())
ans = 0
while N > 0:
    ans += N%2
    N //= 2

print(ans)