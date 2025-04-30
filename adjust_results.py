from sklearn.metrics import classification_report

def adjust_results(results, dogfile):
    """
    Updates the results dictionary by adding two flags:
    - is_dog: 1 if the true label is a valid dog name
    - predicted_dog: 1 if the predicted label is a valid dog name
    """
    with open(dogfile, 'r') as f:
        dog_names = {line.strip().lower() for line in f}

    for value in results.values():
        true_label = value[0].strip().lower()
        classifier_label = value[1].strip().lower()

        is_dog = int(true_label in dog_names)
        predicted_dog = int(classifier_label in dog_names)

        value.extend([is_dog, predicted_dog])

def evaluate_results(results):
    """
    Prints a classification report comparing true labels and predicted labels.
    """
    y_true = []
    y_pred = []

    for val in results.values():
        y_true.append(val[0])
        y_pred.append(val[1])

    print("\n--- Classification Report ---")
    print(classification_report(y_true, y_pred, zero_division=0))