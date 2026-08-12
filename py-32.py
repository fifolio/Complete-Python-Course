def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Func started")
        res = func(*args, **kwargs)
        print("Func ended")
        return res
    return wrapper

@my_decorator
def hello(name, age):
    print(f"Hello, {name}! You are {age}.")

hello("Alice", 30)