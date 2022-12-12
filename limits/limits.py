import numpy as np

'''
a function f(x) has a limit L as the input x approaches a value a if, for every epsilon (ε) greater than 0, there exists a corresponding delta (δ) 
such that for all values of x, if 0 < |x - a| < δ, then |f(x) - L| < ε.

we can say that the limit of the function f(x) = x^2 as the input x approaches 2 is 4, because for every epsilon (ε) greater than 0, we can always find a corresponding delta (δ) such that, for any value of x that is within δ units of 2, the value of the function f(x) will be within ε units of the limit L.


'''
# Define the function f(x) = x^2
def f(x):
    return x**2

def e(n):	
    return (1+(1/n))**n	


'''
f: The function for which we are calculating the limit.
a: The value that the input is approaching.
L: The limit of the function.
epsilon: The epsilon (ε) value used in the definition of the limit.
'''

'''
def limit(f, a, L, epsilon):
    delta = epsilon
    for x in np.arange(a-delta, a+delta, delta/100000):
        if abs(x-a) < delta and abs(f(x)-L) >= epsilon:
            delta = abs(x-a)
    return delta

# Calculate the limit of f(x) as x approaches 2
delta = limit(f, 2, 4, 0.8)
print(delta)
'''


from threading import Timer


def limit_at_infinity(f,dx, timeout=10):
    def timeout_handler():
        raise Exception("can't find a limit")

    # set the timeout timer
    timer = Timer(timeout, timeout_handler)
    timer.start()

    # try to calculate the limit
    try:
        # initialize the limit to 0
        limit = 0

        # start with a large value of x
        x = dx

        # calculate the function at x
        fx = f(x)

        # keep increasing x and recalculating the function
        # until the value of the function does not change anymore
        while True:
            x += dx
            fx_prev = fx
            fx = f(x)
            if fx == fx_prev:
                limit = fx
                break

        return limit
    except Exception as e:
        return e
    finally:
        # stop the timeout timer
        timer.cancel()



print(limit_at_infinity(e, 0.01))

