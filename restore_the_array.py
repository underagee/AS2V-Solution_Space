t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * n
    
    for i in range(n):
        if i == 0:
            ans[i] = arr[i]
        elif i == n - 1:
            ans[i] = arr[i - 1]
        else:
            ans[i] = min(arr[i - 1], arr[i])
    
    print(*ans)
