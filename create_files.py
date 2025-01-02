import os

# Path to the Beginner_Programs folder
folder_path = "Beginner_Programs"

# List of program file names
file_names = [
    "factorial.py",
    "check_prime.py",
    "fibonacci.py",
    "palindrome.py",
    "armstrong.py",
    "reverse_string.py",
    "sum_of_digits.py",
    "gcd.py",
    "calculator.py",
    "leap_year.py",
    "binary_to_decimal.py",
    "decimal_to_binary.py",
    "largest_in_list.py",
    "smallest_in_list.py",
    "count_vowels.py",
    "sort_list.py",
    "perfect_number.py",
    "strong_number.py",
    "sum_of_natural_numbers.py",
    "lcm.py",
    "random_number.py",
    "automorphic_number.py",
    "count_characters.py",
    "harshad_number.py",
    "power_of_number.py",
    "remove_duplicates.py",
    "anagram_checker.py",
    "multiplication_table.py",
    "second_largest.py",
    "abundant_number.py",
    "count_words.py",
    "ascii_value.py",
    "celsius_to_fahrenheit.py",
    "fahrenheit_to_celsius.py",
    "spy_number.py",
    "circle_area.py",
    "rectangle_area.py",
    "triangle_area.py",
    "find_factors.py",
    "perfect_square.py",
    "count_digits.py",
    "reverse_number.py",
    "sum_of_squares.py",
    "hcf.py",
    "neon_number.py",
    "median.py",
    "mode.py",
    "pangram_checker.py",
    "sum_even_numbers.py",
    "sum_odd_numbers.py"
]

# Create the Beginner_Programs directory if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Create each .py file
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        # Placeholder content (empty file)
        file.write("")
        print(f"Created: {file_path}")

print("All .py files have been created.")
