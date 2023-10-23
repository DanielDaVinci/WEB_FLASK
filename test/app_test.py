from functools import wraps


def decor(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("You ara gay, i am inner")
        return func(*args, **kwargs)

    return inner


@decor
def my_func(name, value):
    print(name, "=", value)
    return None


if __name__ == '__main__':
    f = my_func('a', 10)
    print(type(f))
