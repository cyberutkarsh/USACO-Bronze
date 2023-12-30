def feed_cows(num_cows, hunger_levels):
    total_bags = 0  # Total number of bags of corn needed

    # If there's only one cow, no feeding is needed
    if num_cows == 1:
        return 0

    for _ in [1, 2]:
        for i in range(1, num_cows - 1):
            # If current cow is hungrier than the previous one
            if hunger_levels[i] > hunger_levels[i - 1]:
                difference = hunger_levels[i] - hunger_levels[i - 1]
                total_bags += 2 * difference
                hunger_levels[i + 1] -= difference
                hunger_levels[i] = hunger_levels[i - 1]

        # Check if the process made it impossible to equalize hunger levels
        if hunger_levels[num_cows - 1] > hunger_levels[num_cows - 2]:
            return -1

        # Reverse the list for the next iteration
        hunger_levels.reverse()

    # Check if all cows have non-negative hunger levels
    return -1 if hunger_levels[0] < 0 else total_bags

def main():
    print("INPUT:")
    num_test_cases = int(input())  # Number of test cases
    results = []  # Store results for each test case

    for _ in range(num_test_cases):
        num_cows = int(input())
        hunger_levels = list(map(int, input().split()))
        result = feed_cows(num_cows, hunger_levels)
        results.append(result)

    # Print all results at once
    print()
    print("OUTPUT:")
    for result in results:        
        print(result)

if __name__ == "__main__":
    main()