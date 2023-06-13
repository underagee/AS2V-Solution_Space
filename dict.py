# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
group_A = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    group_A[word].append(str(i))

for _ in range(m):
    word = input()
    positions = ' '.join(group_A[word]) if word in group_A else '-1'
    print(positions)

