# d = [4, 1, 7, 3]
# for i in range(3):
#     if d[i] < d[i + 1]:
#         temp = d[i]
#         d[i] = d[i+1]
#         d[i + 1] = temp
# print(d)

# d = [4, 1, 7, 3]
# for i in range(3):
#     if d[i] < d[i + 1]:
#         temp = d[i]
# print(d)

# d = [4, 1, 7, 3]
# for i in range(2):
#     if d[i] > d[i + 1]:
#         temp = d[i]
#         d[i] = d[i+1]
#         d[i + 1] = temp
# print(d)

d = [4, 1, 7, 3]
i = 0
if d[i] > d[i + 1]:
    temp = d[i]
    d[i] = d[i+1]
    d[i + 1] = temp
print(d)
