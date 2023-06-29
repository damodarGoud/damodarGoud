# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# for f in fib():
#     if f > 100:
#         break:
#     print(f)

# ------------------------
# FIZZBUZZ


# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 5 == 0 and i % 3 == 0:
#             print("fizzbuzz")
#         elif i % 5 == 0:
#             print("fizz")
#         elif i % 3 == 0:
#             print("buzz")
#         else:
#             print(i)


# fizzbuzz(20)

# FACTORIAL


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
