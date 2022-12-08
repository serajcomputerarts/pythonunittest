def myf(x,y):
    if type(x) not in [int,float]:
        raise ValueError
    if type(y) not in [int,float]:
        raise ValueError
    if y==0:
        raise ZeroDivisionError
    return x/y

    