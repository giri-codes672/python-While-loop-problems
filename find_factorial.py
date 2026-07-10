# Function to calculate factorial

def find_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    fact = 1
    i = 1

    while i <= n:
        fact *= i
        i += 1

    return fact


# Driver code
try:
    num = int(input("Enter a number: "))
    print("Factorial =", find_factorial(num))
except ValueError as e:
    print(e)
