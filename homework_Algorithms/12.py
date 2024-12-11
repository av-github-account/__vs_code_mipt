# def newton_method(func, derivative, x0, tol=10**(-5), max_i=100):
#     x = x0
#     for i in range(max_i):
#         fx = func(x)
#         dfx = derivative(x)

#         if dfx == 0:
#             print('Производная равна нулю. Метод Ньютона не сходится')
#             return

#         x_next = x - fx / dfx
#         print(f'Шаг {i + 1}: x = {x_next:.10f}, f(x) = {fx:.10f}')

#         if abs(x_next - x) < tol:
#             print(f'\nНайден корень: x = {x_next:.10f} на шаге {i + 1}\n\n')
#             return x_next
#         x = x_next
#     print('Метод Ньютона не сошелся за заданное число итераций')

# def f(x):
#     return 5*x - 6*x**2 + 2

# def df(x):
#     return 5 - 12*x

# def main():
#     x0_1 = 1
#     newton_method(f, df, x0_1) 
#     x0_2 = 2
#     newton_method(f, df, x0_2)

# if __name__ == '__main__':
#     main()



# dif = 1
# x = 100
# counter = 0

# while abs(dif) > 10**(-5):
#     counter += 1
#     dif = (5*x - 6*(x**2)+2)/(5-12*x)
#     x -= dif
#     print(f'\nx = {x}, dif = {dif}, num of iters = {counter}')

# def newton_method(f, f_prime, x0, tolerance=1e-5):
#     steps = []
#     xn = x0
#     for n in range(100):  # Ограничение на количество итераций для предотвращения зацикливания
#         fxn = f(xn)
#         f_prime_xn = f_prime(xn)

#         if abs(f_prime_xn) < 1e-10: # Проверка деления на 0 или очень маленькое число
#           return None

#         xn1 = xn - fxn / f_prime_xn
#         steps.append(xn1)

#         if abs(xn1 - xn) < tolerance:
#             return xn1, n + 1, steps

#         xn = xn1

#     return None

# # Пример использования для уравнения 5x - 6x^2 + 2 = 0
# def f(x):
#     return 5 * x - 6 * x**2 + 2

# def f_prime(x):
#     return 5 - 12 * x

# x0 = 1
# result = newton_method(f, f_prime, x0)

# if result:
#   root, step, steps = result
#   print("Задача 1.")
#   print(f"• Корень найден на шаге {step}: x = {root}")
#   print("• Все шаги:")
#   for i, x in enumerate(steps):
#     print(f"  Шаг {i+1}: x = {x}")

#   x0 = 2
#   result = newton_method(f, f_prime, x0)
#   if result:
#     root, step, steps = result
#     print(f"• При x0 = 2, корень найден на шаге {step}: x = {root}")
#   else:
#      print("• При x0 = 2, метод не сошелся")

# else:
#     print("Метод не сошелся")

# def func(x, y):
#     return 2*x 

# def euler_method(x0, y0, h, N):
#     x = x0
#     y = y0

#     for _ in range(N):
#         y += h * func(x, y)
#         x += h
    
#     return y

# x0 = 0
# y0 = 1
# h = 0.1
# N = 10

# result = euler_method(x0, y0, h, N)
# print(result) # Выводится значение y(x=1)


# ===
# def f(x, y):
#     return 2*x

# def euler_method(f, x0, y0, h, N):
#     x = x0
#     y = y0
#     for _ in range(N):
#         y += f(x, y) * h
#         x += h
#     return y

# x0 = 0
# y0 = 1
# h = 1/10  # шаг
# N = 10  # количество шагов
# x1 = 1

# result = euler_method(f, x0, y0, h, N)
# print(result)

# ответ: 1.9000000000000001 


# N =int(input("Введите N (число шагов): "))

# def f(x, y):
#     return x*x + 1

# def euler_method(f, x0, y0, h, N):
#     x = x0
#     y = y0
#     for _ in range(N):
#         y += f(x, y) * h
#         x += h
#     return y

# x0 = 0
# y0 = 1
# h = 1/N  # шаг
# # N = 10  # количество шагов
# x1 = 1

# result = euler_method(f, x0, y0, h, N)
# print(result)



from scipy.optimize import linprog

# Коэффициенты целевой функции
c = [0.04, 0.15, 0.40]

# Коэффициенты ограничений
A = [
    [-0.38, -0.001, -0.002],  # Кальций
    [0, -0.09, -0.5],        # Белок
    [0, -0.02, -0.08]        # Клетчатка
]

# Правая часть ограничений
b = [-80, -2200, -500]

# Ограничения на веса
A_eq = [[1, 1, 1]]
b_eq = [10000]

# Решение
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')

# Вывод результатов
if result.success:
    print('Минимальная стоимость: ', result.fun)
    print('Распределение ингредиентов:')
    print('Известняк (кг):', result.x[0])
    print('Зерно (кг):', result.x[1])
    print('Соевые бобы (кг):', result.x[2])
else:
    print('Решение не найдено:', result.message)
