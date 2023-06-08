if __name__ == '__main__':
    N = int(input())

    List =[]
    
    for i in range(N):
        prompt = input().split()
        
        if prompt[0] == "insert":
            List.insert(int(prompt[1]),int(prompt[2]))
        
        elif prompt[0] == "remove":
            List.remove(int(prompt[1]))
            
        elif prompt[0] == "append":
            List.append(int(prompt[1]))
            
        elif prompt[0] == "sort":
            List.sort()
            
        elif prompt[0] == "pop":
            List.pop()
            
        elif prompt[0] == "reverse":
            List.reverse()
            
        elif prompt[0] == "print":
            print(List)
        
