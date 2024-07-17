from PIL import Image, ImageEnhance
import numpy as np
import cv2
import os

def main():
    """
    Script to load, enhance, and process an image of the Rosetta Stone.
    This script performs the following steps:
    1. Load the image and convert it to grayscale.
    2. Enhance the contrast and brightness of the image.
    3. Apply CLAHE (adaptive histogram equalization).
    4. Apply sharpening.
    5. Apply simple thresholding.
    6. Display the original and thresholded images.
    7. Wait for the user to press 'q' or 'Esc' to close the windows.
    
    Note: In case the windows do not respond to 'q' or 'Esc', use 'Cmd+Q' on Mac to close the windows.
    """
    # Ensure the current working directory is correct
    print(f"Current working directory: {os.getcwd()}")
    image_directory = 'Session 00 - Rosetta Stone/'
    # Verify the file exists in the current directory
    image_path = os.path.join(image_directory, 'Champollion-hieroglyphs-750x947.jpg')
    if not os.path.exists(image_path):
        print(f"File not found: {os.path.abspath(image_path)}")
        # List the contents of the current directory
        print("Files in the current directory:")
        print(os.listdir('.'))
        exit()

    print(f"File found: {os.path.abspath(image_path)}")

    # Load the image using PIL and convert to grayscale
    try:
        image = Image.open(image_path).convert('L')  # Convert to grayscale
        print(f"Successfully loaded image: {image_path}")
    except IOError:
        print(f"Cannot open {image_path}")
        exit()

    # Enhance the contrast and brightness of the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Adjust the enhancement factor as needed
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # Adjust the enhancement factor as needed

    # Convert the PIL image to a NumPy array
    image_np = np.array(image)

    # Apply CLAHE (adaptive histogram equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image_np = clahe.apply(image_np)

    # Apply sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    image_np = cv2.filter2D(image_np, -1, kernel)

    # Apply simple thresholding
    threshold_value = 128
    _, thresholded_image = cv2.threshold(image_np, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images using OpenCV
    cv2.imshow('Enhanced Original Image', image_np)
    cv2.imshow('Thresholded Image', thresholded_image)

    # Add a loop to wait for a specific key press to close windows
    print("Press 'q' or 'Esc' to close the windows")
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' key or 'Esc' key to exit
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Save the thresholded image
    cv2.imwrite(image_directory + 'thresholded_champollion_hieroglyphs.jpg', thresholded_image)

    print("Image processing complete and windows closed.")

if __name__ == "__main__":
    main()
