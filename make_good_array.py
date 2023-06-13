def find_next_power_of_two(x):
    current = 1
    while current <= x:
        current *= 2
    return current

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(n)
    for i in range(n):
        print(i+1, find_next_power_of_two(a[i]) - a[i])
