import os
import shutil

def handle_misclassifications(results, image_dir, output_dir='misclassified/'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename, values in results.items():
        pet_label, classifier_label, match = values[0], values[1], values[2]
        if match == 0 and values[3] == 1 and values[4] == 1:
            src = os.path.join(image_dir, filename)
            dst = os.path.join(output_dir, filename)
            shutil.copy(src, dst)