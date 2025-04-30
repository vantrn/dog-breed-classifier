import os
import re

def get_pet_labels(image_dir):
    pet_labels = {}

    for filename in os.listdir(image_dir):
        if filename.startswith('.') or not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            continue

        # Clean and normalize filename
        name = os.path.splitext(filename)[0]  # remove file extension
        name = re.sub(r'[-_]', ' ', name)     # replace - and _ with space
        name = re.sub(r'\d+', '', name)       # remove numbers
        name = re.sub(r'\s+', ' ', name).strip().lower()  # normalize spaces

        # Extract only alphabetic words
        words = [word for word in name.split() if word.isalpha()]
        label = " ".join(words)

        pet_labels[filename] = [label]

    return pet_labels