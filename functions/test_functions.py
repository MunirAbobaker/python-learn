from  functions.functions import funcs

def test():
    
    x = 2
    for func in sorted(funcs):
        print(func, funcs[func](x))
