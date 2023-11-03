# Get user input for the desired length of the Fibonacci series
N = int(input("Enter the length of the Fibonacci series: "))

# Initialize the first two Fibonacci numbers
fibonacci_series = [1, 1]

# Generate the Fibonacci series up to the specified length
while len(fibonacci_series) < N:
    next_number = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_number)

# Print the generated Fibonacci series
print("Fibonacci Series:")
for number in fibonacci_series:
    print(number, end=" ")
