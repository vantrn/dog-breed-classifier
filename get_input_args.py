import argparse

def get_input_args():
    parser = argparse.ArgumentParser(description="Process command line arguments for image classification.")

    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to the folder containing pet images.')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='CNN model architecture (resnet, alexnet, vgg).')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='File containing valid dog breeds.')

    return parser.parse_args()