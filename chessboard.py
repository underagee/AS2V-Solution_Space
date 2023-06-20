t = int(input())

for _ in range(t):
    input()
    chessboard = []
    column_counts = {}
    solution = []
    
    for i in range(8):
        row = list(input())
        chessboard.append(row)
        
        column_counts[i] = row.count("#")
        
    for i in range(1, 7):
        # Counting rows
        if column_counts[i] == 1 and column_counts[i - 1] == 2 and column_counts[i + 1] == 2:
            solution.append(i)
            break
        
    row_with_bishop = chessboard[solution[0]]
    
    for i in range(len(row_with_bishop)):
        if row_with_bishop[i] == "#":
            solution.append(i)
            break
    
    print(solution[0] + 1, solution[1] + 1)
