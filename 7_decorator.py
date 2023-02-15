def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


# def ordinary():
#     print("I am ordinary")


# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# # call the decorated function
# decorated_func()

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  
