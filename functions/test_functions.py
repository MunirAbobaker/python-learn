from  functions.functions import funcs, f, square, cube, is_even, my_add, custom_sum

def test():
    
    x = 2
    for func in sorted(funcs):
        print(func, funcs[func](x))


def test2():
    print(f())
    print(f())
    print(f())
    print(f(x = [9,9,9]))
    print(f())
    print(f())

def test3():
    # The map function applies a function to each member of a collection

    map(square, range(5))
    filter(is_even, range(5))
    return map(square, filter(is_even, range(5)))


def test4():
    #reduce(my_add, [1,2,3,4,5])
    xs = range(5)
    print(custom_sum(xs, square))
    print(custom_sum(xs, cube))