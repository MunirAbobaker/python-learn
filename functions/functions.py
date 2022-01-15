
def square(x):
    """Square of x."""
    return x*x

def cube(x):
    """Cube of x."""
    return x*x*x

funcs = {
    'square': square,
    'cube': cube,
}


#Binding of default arguments occurs at function definition
def f2(x = []):
    x.append(1)
    return x


# Usually, this behavior is not desired and we would write
def f(x = None):
    if x is None:
        x = []
    x.append(1)
    return x

def is_even(x):
    return x%2 == 0

def my_add(x, y):
    return x + y

# Custom functions can of couse, also be HOFs
def custom_sum(xs, transform):
    """Returns the sum of xs after a user specified transform."""
    return sum(map(transform, xs))