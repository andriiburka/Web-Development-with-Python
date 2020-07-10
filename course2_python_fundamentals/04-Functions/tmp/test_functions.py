# this is a greeting function
def say_hello(name):
    return f'hello, {name}'


def greet_andrew(calling_say_hello):
    return calling_say_hello('Andrew')


# 1 - calling the func greet_andrew(will use say_hello as structure sentense)
print(greet_andrew(say_hello))
