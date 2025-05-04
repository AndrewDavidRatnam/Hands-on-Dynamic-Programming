def minOperations(n):
    # MinOp = 0
    # i = n
    # while (i > 1):
    #     if (i-1) % 3 == 0:
    #         i-=1
    #         i /= 3
    #         MinOp += 2
    #         continue
    #     if i % 3 ==0:
    #         i /= 3
    #         MinOp +=1
    #         continue
    #     elif i%2 == 0:
    #         i /= 2
    #         MinOp +=1
    #         continue
    #     else:
    #         i -= 1
    #         i /= 2
    #         MinOp += 2
        
    # return MinOp
    min_op = [0]*(n+1)
    if n == 1:
        return 0
    if n == 2 :
        return 1 
    min_op[1] = 0

    for i in range(2,n+1):
        min_op[i] = 1 + min_op[i-1]
        
        if i%2 ==0:
            min_op[i] =  min(min_op[i], 1+min_op[i//2])
        if i%3 ==0:
            min_op[i] = min(min_op[i], 1+ min_op[i//3])
        # print(min_op[:i+1])
        # min_op[i] = 1 + min(min_op[i-1], if i%2 == 0 min_op[i//2], if i%3 == 0,min_op[i//3])
    return min_op[-1] 


n = int(input())
print(minOperations(n))