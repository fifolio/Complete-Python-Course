def outer():
    print("This is the Outer function.")
    def inner():
        print("This is the Inner function.")
    inner()

outer()