# Keyword arguments
def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(name="Alice", age=30)

# Default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")

# Variable-length arguments
def sum_numbers(*args):
    total = sum(args)
    print(f"Sum: {total}")
sum_numbers(1, 2, 3)

# Variable-length keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")