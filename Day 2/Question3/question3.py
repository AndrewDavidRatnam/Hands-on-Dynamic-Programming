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



n = int(input())
print(minOperations(n))