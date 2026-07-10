# Function to print numbers from 1 to n

def print_numbers(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

# Driver code
num = int(input("Enter a positive number: "))

if num > 0:
    print_numbers(num)
else:
    print("Please enter a positive integer.")
