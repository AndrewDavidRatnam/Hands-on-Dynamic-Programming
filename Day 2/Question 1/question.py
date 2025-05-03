def climb_stairs(n):
    total_ways = [0] * (n)
    total_ways[0] = 1
    total_ways[1] = 2
    for i in range(3,n+1):
        print(f"Step{i}")
        total_ways[i-1] = total_ways[i-2] + total_ways[i-3] 
        print(total_ways[i-1])
    
    
    
    return total_ways[-1] #not completed     
n = int(input())
print(climb_stairs(n))