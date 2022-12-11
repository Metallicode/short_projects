# Define the function f(x) = x^2
def f(x):
    return x**2

def limit(f, a, L, epsilon):
    delta = epsilon
    for x in range(a-delta, a+delta):
        if abs(x-a) < delta and abs(f(x)-L) >= epsilon:
            delta = abs(x-a)
    return delta

# Calculate the limit of f(x) as x approaches 2
delta = limit(f, 2, 4, 0.5)


def limit(f, a, L):
    for x in range(a, a+1000):
        if abs(f(x)-L) >= 0.001:
            return False
    return True


# Calculate the limit of f(x) as x approaches infinity
result = limit(f, 100, 0)
if result:
    print("The limit of f(x) as x approaches infinity is 0")
else:
    print("The limit of f(x) as x approaches infinity does not exist")
