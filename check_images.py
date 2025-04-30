from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results import adjust_results, evaluate_results
from validate_labels import validate_labels
from print_results import print_results
from handle_misclassifications import handle_misclassifications
from generate_summary import generate_summary, plot_confusion_matrix

def main():
    # Start the timer
    start_time = time()

    # Step 1: Get command-line arguments
    in_arg = get_input_args()

    # Step 2: Create pet labels from image filenames
    pet_labels = get_pet_labels(in_arg.dir)

    # Step 3: Classify images using a pretrained CNN model
    results = classify_images(in_arg.dir, pet_labels, in_arg.arch)

    # Step 4: Adjust results with dogfile comparison
    adjust_results(results, in_arg.dogfile)

    # Step 5: Validate dog names using the dogfile
    validate_labels(results, in_arg.dogfile)

    # Step 6: Print a results summary
    print_results(results)

    # Step 7: Optional extra features
    handle_misclassifications(results, in_arg.dir)
    generate_summary(results)
    plot_confusion_matrix(results)
    evaluate_results(results)

    # Stop the timer and print total runtime
    end_time = time()
    print(f"\n** Total Elapsed Runtime: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
