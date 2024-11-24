# def knapsack(values, weights, capacity):
#     n = len(values)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i-1] > w:
#                 dp[i][w] = dp[i-1][w]
#             else:
#                 dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])

#     selected_items = []
#     w = capacity
#     for i in range(n, 0, -1):
#         if dp[i][w] != dp[i-1][w]:
#             selected_items.append(i-1)
#             w -= weights[i-1]

#     return dp[n][capacity], selected_items

# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

# max_value, selected_items = knapsack(values, weights, capacity)

# print(f"Максимальная стоимость: {max_value}")
# print("Выбранные предметы:")
# for i in selected_items:
#     print(f"Вещь {i+1}: ({values[i]}, {weights[i]})")



def backpack(weights, values, capacity):
    n = len(weights)
    ratio = [values[i] / weights[i] for i in range(n)]
    sorted_items = sorted(range(n), key=lambda x: ratio[x], reverse=True)
    
    total_weight = 0
    total_value = 0
    items_in_backpack = []
    
    for i in sorted_items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_value += values[i]
            items_in_backpack.append(i)
    
    return items_in_backpack, total_value

values = [10000, 12000, 5000]
weights = [2, 3, 1]
capacity = 3
selected_items, total_value = backpack(weights, values, capacity)

print("Selected items:", selected_items)
print("Total value:", total_value)
