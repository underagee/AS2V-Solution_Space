# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())

shoe_sizes = list(map(int, input().split()))

shoe_counter = Counter(shoe_sizes)

m = int(input())

earnings = 0

for _ in range(m):
    size, price = map(int, input().split())
    if shoe_counter[size] > 0:
        shoe_counter[size] -= 1
        earnings += price

print(earnings)
