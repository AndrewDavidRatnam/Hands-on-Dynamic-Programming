min_index_table = []

length = input("Enter number of stones")
heights = []
for x in range(length):
    height = input("Enter the heights")
    heights.append(height)
print(f"Heights list: {heights}")

def minCost(heights): #[10, 30, 40, 20]
    current_stone = heights[0]

    min_cost = 0

    min_index = return_min_index(heights[1:])

    min_cost = abs(current_stone - heights[min_index])

def return_min_index(heights):#[30, 40, 20]




