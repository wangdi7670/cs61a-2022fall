square = lambda x: x * x
from operator import add, mul


def greater_than_5(x):
    return x > 5


def accumulate(merger, start, n, term):
    ans = start
    for i in range(1, n + 1):
        ans = merger(ans, term(i))
    
    return ans


def filtered_accumulate(merger, start, cond, n, term):
    def merge_if(x, y):
        "*** YOUR CODE HERE ***"
        if cond(y):
            return merger(x, y)
        else:
            return x
        
    return accumulate(merge_if, start, n, term)


a =  filtered_accumulate(mul, 1, greater_than_5, 5, square)
print(a)