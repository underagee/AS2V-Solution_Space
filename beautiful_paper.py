t = int(input())
 
for _ in range(t):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    
    # Checking if the sum of any two sides of the rectangles is equal
    if (a1 == a2 and b1 + b2 == a1) or (a1 == b2 and b1 + a2 == a1) or \
           (b1 == a2 and a1 + b2 == b1) or (b1 == b2 and a1 + a2 == b1):
            print("YES")
    else:
            print("NO")
