import csv
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt 
import re

def generate_summary(results, output_file='summary.csv'):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Pet Label', 'Classifier Label', 'Match', 'Is Dog', 'Predicted Dog']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for fname, vals in results.items():
            writer.writerow({
                'Filename': fname,
                'Pet Label': vals[0],
                'Classifier Label': vals[1],
                'Match': vals[2],
                'Is Dog': vals[3],
                'Predicted Dog': vals[4]
            })

def normalize(label):
    """Standardize labels: lowercase, no extra spaces, no punctuation."""
    label = label.lower()
    label = re.sub(r'[^a-z ]', '', label)  # remove non-letters
    label = re.sub(r'\s+', ' ', label).strip()  # remove extra spaces
    return label

def plot_confusion_matrix(results):
    y_true = [normalize(v[0]) for v in results.values()]
    y_pred = [normalize(v[1]) for v in results.values()]
    labels = sorted(list(set(y_true + y_pred)))

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

    fig, ax = plt.subplots(figsize=(12, 10))
    disp.plot(xticks_rotation=90, ax=ax)
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()