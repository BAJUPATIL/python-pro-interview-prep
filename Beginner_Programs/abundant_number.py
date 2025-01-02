# Program to check if a number is an abundant number.
# An abundant number is a number whose sum of proper divisors is greater than the number itself.
# Example: 12 is an abundant number (1 + 2 + 3 + 4 + 6 = 16 > 12).

# Take input from the user and convert it to an integer
n = int(input("Enter number here: "))

# Initialize the sum of divisors to 0
sum_divisors = 0

# Loop through all numbers from 1 to n-1
for i in range(1, n):
    # If i is a divisor of n, add it to the sum of divisors
    if n % i == 0:
        sum_divisors += i

# Check if the sum of divisors is greater than the number itself
# Print the result accordingly
print(f"{n} is an abundant number") if sum_divisors > n else print(f"{n} is not an abundant number")

