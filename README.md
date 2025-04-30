# 🐶 Dog Breed Classifier

This project is a deep learning-based image classifier that identifies dog breeds using Convolutional Neural Networks (CNNs) and transfer learning. It uses pre-trained models like **ResNet**, **VGG**, and **AlexNet**, and provides tools for training, prediction, evaluation, and visualizing misclassifications.

Built by **Van Tran**, a Software Engineering student at UTD, this project, through IEEE projects, was created to explore CNNs and transfer learning for image classification using a real-world dataset.

---

## 📂 About the `pet_images/` Folder

The `data/pet_images/` folder is **empty by default**.

To use the classifier, **you must add your own image folders**, where each folder name is the name of the dog breed (e.g., `labrador`, `husky`, `poodle`).

Each folder should contain images in one of the following formats:
- `.jpg`
- `.png`
- `.webp`

Example structure:

---

## 🛠️ How to Set Up and Run

1. **Install Python packages**
   ```bash
   pip install -r requirements.txt

2. **Add your pet breed image folders into data/pet_images/ (see above).**

3. **Train your model**  
   Choose a model and run training:
   ```bash
   python main.py --model resnet --train

5. **Run predictions**
  ```bash
  python main.py --model resnet --predict
```

6. **Evaluate performance**
  ```bash
python evaluate.py --model resnet
