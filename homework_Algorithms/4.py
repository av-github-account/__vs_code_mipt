# import random

# def generated_nums (nums) :
#     for i in range (10):
#         nums.append (random.randint (1, 100))

#     return nums

# def bubble_sort (numbers) :
#     n = len (numbers)
#     step = 0
#     for i in range(n) :
#         for j in range(0, n - i - 1):
#             if numbers[j] > numbers [j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers [j]
#             step += 1
#             print (f"Итерация {step}: {numbers}")

# # def main():
# nums = []
# generated_nums (nums)
# print (f'Изначальный массив: \n{nums}\n' )
# bubble_sort(nums)

# # if __name__ == ' main ':
# #         main()


# def shell_sort(arr):
#     n = len(arr)
#     g = n // 2

#     while g > 0:
#         for i in range(g, n):
#             temp = arr[i]
#             j = i
#             while j >= g and arr[j - g] > temp:
#                 arr[j] = arr[j - g]
#                 j -= g
#             arr[j] = temp
#         g //= 2

#     return arr



# arr = [7, 1, 20, 100, 3, 32, 97, 0, 2]
# print(f"Список на входе: \n{arr}\n")
# sorted_arr = shell_sort(arr)
# print(f"Отсортированный список: \n{sorted_arr}")



# import random
# def generated_nums (nums) :
#     for i in range (10):
#         nums.append (random.randint (1, 100))
#     return nums

# def quick_sort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr

#     piv = arr[n // 2]
#     l = [x for x in arr if x < piv]
#     m = [x for x in arr if x == piv]
#     r = [x for x in arr if x > piv]

#     return quick_sort(l) + m + quick_sort(r)

# def main():
#     nums = []
#     generated_nums(nums)
#     arr = nums #[7, 1, 20, 100, 3, 32, 97, 0, 2]
#     print(f"Список на входе: \n{arr}\n")
#     sorted_arr = quick_sort(arr)
#     print(f"Отсортированный список: \n{sorted_arr}")

# if __name__ == '__main__':
#     main()


def knapsack(cap, wt, cost):
    n = len(cost)
    dp = [[0 for x in range(cap + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(cap + 1):
            # print (dp[i][j])
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif wt[i - 1] <= j:
                dp[i][j] = max(cost[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
                print (dp[i][j])
            else:
                dp[i][j] = dp[i - 1][j]
                # print (dp[i][j])

    return dp[n][cap]

def main():
    cost = [10, 12, 5]
    weight = [2, 3, 1]
    capacity = 3

    max_v = knapsack(capacity, weight, cost)
    print(f"Максимальная ценность: {max_v}")

if __name__ == '__main__':
    main()


# def knapsack(W, weights, values, n):
#     dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, W + 1):
#             if weights[i-1] <= j:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1])
#             else:
#                 dp[i][j] = dp[i-1][j]

#     max_value = dp[n][W]

#     selected_items = []
#     j = W
#     for i in range(n, 0, -1):
#         if dp[i][j] != dp[i-1][j]:
#             selected_items.append(i-1)
#             j -= weights[i-1]

#     return max_value, selected_items

# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 6]
# W = 5
# n = len(weights)

# max_value, items = knapsack(W, weights, values, n)
# print("Максимальная стоимость:", max_value)
# print("Выбранные предметы (индексы):", items)
