

# LENGTH = int(input("Enter number of stones"))
# heights = []
heights = [30, 10, 60, 10, 60, 50]
# for x in range(LENGTH):
#     height = input("Enter the heights")
#     heights.append(height)
# print(f"Heights list: {heights}")

def minCost(heights): #[10, 30, 40, 20]
    length = len(heights)
    min_index_table = [-1 for x in range(length)]
    for i, height in enumerate(heights):
        print(i)
        print(min_index_table)
        if i == (length - 2 ):
            min_index_table[i] = i+1
            break
        if i == (length - 1 ):
            break
        if abs(height - heights[i+1]) == abs(height - heights[i+2]):
            min_index_table[i] = i+2
            continue 
            #expression_if_true if condition else expression_if_false
        min_index_table[i] = i+1 if (abs(height - heights[i+1]) < abs(height - heights[i+2])) else (i+2)

    return min_index_table
        

print(minCost(heights))





