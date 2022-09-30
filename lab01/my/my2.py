print('hello, Python')

for  i in range(1, 4):
    print(i);

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        ans = 1
        for i in range(k):
            ans = ans * (n - i)
        
        return ans

print(falling(4, 3))