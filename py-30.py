nums = [1, 2, 3, 4, 5]

# Map: Multiply each number by 2
mapped = list(map(lambda x: x * 2, nums))

# Reduce: Sum all the numbers
from functools import reduce
reduced = reduce(lambda x, y: x + y, mapped)

print("Mapped:", mapped)
print("Reduced:", reduced)
