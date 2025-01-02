import os

# Define the directories and their respective file names
directories = {
    "Beginner_Programs": [
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
    ],
    "Intermediate_Programs": [
        "matrix_addition.py",
        "matrix_multiplication.py",
        "binary_search.py",
        "merge_sort.py",
        "quick_sort.py",
        "heap_sort.py",
        "linear_search.py",
        "string_permutations.py",
        "merge_two_lists.py",
        "longest_palindrome.py",
        "check_subsequence.py",
        "generate_combinations.py",
        "rotate_matrix.py",
        "transpose_matrix.py",
        "largest_sum_subarray.py",
        "longest_common_subsequence.py",
        "knapsack_problem.py",
        "tower_of_hanoi.py",
        "sudoku_solver.py",
        "n_queens_problem.py",
        "max_heap.py",
        "min_heap.py",
        "binary_tree_traversal.py",
        "graph_dfs.py",
        "graph_bfs.py",
        "detect_cycle_in_graph.py",
        "shortest_path_dijkstra.py",
        "shortest_path_bellman_ford.py",
        "longest_path_dag.py",
        "edit_distance.py",
        "pattern_matching.py",
        "wildcard_matching.py",
        "largest_histogram.py",
        "max_area_rectangle.py",
        "trapping_rainwater.py",
        "job_scheduling.py",
        "activity_selection.py",
        "minimum_spanning_tree.py",
        "prim_algorithm.py",
        "kruskal_algorithm.py"
    ],
    "Advanced_Programs": [
        "web_scraper.py",
        "data_encryption.py",
        "machine_learning_model.py",
        "deep_learning_model.py",
        "rest_api.py",
        "graphql_api.py",
        "ai_chatbot.py",
        "image_classification.py",
        "time_series_forecasting.py",
        "natural_language_processing.py",
        "speech_recognition.py",
        "object_detection.py",
        "game_simulation.py",
        "genetic_algorithm.py",
        "neural_network_from_scratch.py",
        "database_migration.py",
        "cloud_integration.py",
        "blockchain_implementation.py",
        "multithreading.py",
        "distributed_system_simulation.py",
        "kafka_streaming.py",
        "real_time_dashboard.py",
        "virtual_reality_app.py",
        "augmented_reality_app.py",
        "quantum_computation.py",
        "cybersecurity_tool.py",
        "network_simulation.py",
        "docker_container_management.py",
        "kubernetes_orchestration.py",
        "serverless_architecture.py"
    ]
}

# Loop through each directory and create the files
for folder_name, file_names in directories.items():
    # Create the directory if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Create each .py file inside the directory if it doesn't already exist
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                # Placeholder content (empty file)
                file.write("")
                print(f"Created: {file_path}")
        else:
            print(f"Skipped (already exists): {file_path}")

print("All directories and files have been processed successfully!")
