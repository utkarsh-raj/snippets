#Chef and Typing
t = int(input())
left = ['d','f']
right = ['j','k']
for p in range(t):
    n = int(input())
    words = []
    Tcost = 0
    for q in range(n):
        word = input()
        arr = list(word)
        cost = 2
        currenthand = 0
        if arr[0] in left:
            currenthand = 0
        else:
            currenthand = 1
        for i in range(1,len(arr)):
            if arr[i] in left:
                if currenthand == 0:
                    cost +=4
                else:
                    cost +=2
                currenthand = 0
            else:
                if currenthand == 0:
                    cost +=2
                else:
                    cost += 4
                currenthand = 1
        if word in words:
            cost = cost//2
        words.append(word)
        Tcost += cost
    print(Tcost)
            
    
