def print_results(results):
    total = len(results)
    correct_matches = sum([1 for v in results.values() if v[2] == 1])
    correct_dogs = sum([1 for v in results.values() if v[3] == 1 and v[4] == 1])
    incorrect_dogs = sum([1 for v in results.values() if v[3] == 1 and v[4] == 0])

    print("\n--- Results Summary ---")
    print(f"Total Images: {total}")
    print(f"Correct Label Matches: {correct_matches}")
    print(f"Correctly Classified Dogs: {correct_dogs}")
    print(f"Incorrectly Classified Dogs: {incorrect_dogs}")
    print(f"Accuracy: {100 * correct_matches / total:.2f}%")