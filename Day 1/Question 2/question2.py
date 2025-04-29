def minCost(heights):
  length = len(heights)
  distance_table = [0 for x in range(length)]
  distance_table[0] = 0
  for i in range(length):
    distance_table[i] = min(distance_table[i-1] + abs(heights[i] - heights[i-1]), distance_table[i-2] + abs(heights[i] - heights[i-2]) if i > 1 else float("inf"))
  return distance_table[-1]

heightss = [[10, 30, 40, 20],[10, 10],[30, 10, 60, 10, 60, 50] ]

print(minCost(heights))





