nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(n):
#     return n % 2 == 0

evens = filter(lambda n: n % 2 == 0, nums)

print(list(evens))