from classifier import classifier

def classify_images(image_dir, pet_labels, model):
    results = {}

    for filename, label in pet_labels.items():
        image_path = f"{image_dir}/{filename}"

        # Get classification label
        classifier_label = classifier(image_path, model).lower().strip()

        # Check if the classification matches the pet label
        match = 1 if label[0] in classifier_label else 0

        # Store results
        results[filename] = [label[0], classifier_label, match]

    return results