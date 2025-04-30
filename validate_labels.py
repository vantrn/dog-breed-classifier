def validate_labels(results, dogfile):
    """
    Validates that pet labels and classifier labels are in the dog names list.
    Prints a warning if either is not found in the dognames.txt file.
    """
    # Read all valid dog names into a set
    with open(dogfile, 'r') as f:
        dog_names = {line.strip().lower() for line in f}

    for filename, values in results.items():
        true_label = values[0].strip().lower()
        classifier_label = values[1].strip().lower()

        if true_label not in dog_names:
            print(f"[WARNING] Pet label '{true_label}' in '{filename}' not found in dognames.txt")

        if classifier_label not in dog_names:
            print(f"[WARNING] Classifier label '{classifier_label}' in '{filename}' not found in dognames.txt")
