

def nth_fibonacci(n):
    a = 0
    b = 1
    for i in range(1,n):
        c = a + b
        a = b
        b = c 
    return c

n = int(input())
print(nth_fibonacci(n))

# 0,1,1,2,3,5,8