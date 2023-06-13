n = int(input())
arr = list(map(int, input().split()))

positive_set = []
negative_set = []
zero_set = []

for num in arr:
    if num < 0:
        negative_set.append(num)
    elif num > 0:
        positive_set.append(num)
    else:
        zero_set.append(num)

if len(positive_set) == 0:
    positive_set.append(negative_set.pop())
    positive_set.append(negative_set.pop())

if len(negative_set) % 2 == 0:
    zero_set.append(negative_set.pop())

print(len(negative_set), *negative_set)
print(len(positive_set), *positive_set)
print(len(zero_set), *zero_set)
