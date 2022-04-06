# Without dynamic programing applications
def fibonacci(n):
    '''Assumes n > 1 as int,
    returns fibonnaci equivalent of n.'''    
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# According to memoization method (topdown)
def fib_memo(n, memo = {}):
    """Assumes n is an int >= 0,
        memo used only by recursive calls
        Return Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result

#According to tabular method (bottom - up)

def fib_tab(n):
    """Assumes n is an int >= 0
       Returns Fibonacci of n"""
    tab = [1]*(n+1) # only first two values matter
    for i in range(2, n + 1):
        tab[i] =tab[i-1] + tab[i-2]
    return tab[n]
