if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    List = []
    largest_number = max(arr)
    for i in arr:
        if i < largest_number:
            List.append(i) 
    runnerup = max(List)
    print(runnerup)
