from torchvision import models, transforms
from PIL import Image
import torch

def classifier(image_path, model_name='vgg'):
    # Load image
    img = Image.open(image_path).convert('RGB')
    
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    img_tensor = preprocess(img).unsqueeze(0)

    # Select model
    if model_name == 'resnet':
        model = models.resnet18(pretrained=True)
    elif model_name == 'alexnet':
        model = models.alexnet(pretrained=True)
    else:
        model = models.vgg16(pretrained=True)

    model.eval()

    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = outputs.max(1)

    # Load class labels from ImageNet
    from torchvision.models import ResNet18_Weights, AlexNet_Weights, VGG16_Weights
    weights = {
        'resnet': ResNet18_Weights.DEFAULT,
        'alexnet': AlexNet_Weights.DEFAULT,
        'vgg': VGG16_Weights.DEFAULT
    }
    labels = weights[model_name].meta['categories']

    return labels[predicted.item()]