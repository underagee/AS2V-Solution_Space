from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    line = input().split()
    item = " ".join(line[:-1])
    price = int(line[-1])
    items[item] = items.get(item, 0) + price

for item, price in items.items():
    print(item, price)
