import cv2
import os

def preprocess_image(image_path):
    """
    Preprocess the image by converting to grayscale and applying thresholding.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    return thresholded_image

def segment_and_save_characters(image, section, section_name, output_dir):
    """
    Segment individual characters from a specific section of the image and save them.
    Args:
    - image: The preprocessed image.
    - section: Tuple containing the coordinates of the section (x, y, w, h).
    - section_name: Name of the section for creating output directories.
    - output_dir: Directory to save the output character images.
    """
    x, y, w, h = section
    roi = image[y:y+h, x:x+w]
    
    # Find contours (assuming characters are connected components)
    contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a directory for the section if it doesn't exist
    section_dir = os.path.join(output_dir, section_name)
    os.makedirs(section_dir, exist_ok=True)
    
    # Save each character as an image
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        char_image = roi[y:y+h, x:x+w]
        char_image_path = os.path.join(section_dir, f'{section_name}_char_{i+1}.png')
        cv2.imwrite(char_image_path, char_image)
        print(f"Character {i+1} from {section_name} saved to {char_image_path}")

def main():
    image_directory = 'Session 00 - Rosetta Stone/'

    # Path to the preprocessed image
    image_path = os.path.join(image_directory, 'thresholded_champollion_hieroglyphs.jpg')

    # Load the preprocessed image
    image = preprocess_image(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Create output directory if it doesn't exist
    output_dir = os.path.join(image_directory, 'ocr_output')
    os.makedirs(output_dir, exist_ok=True)

    # Define the sections of the image (x, y, width, height)
    sections = {
        "Greek_Letters": (209, 137, 505, 747),
        "Demotic_Signs": (63, 142, 140, 743),
        "Hieroglyphic_Signs": (14, 146, 32, 745),
    }

    # Segment and save characters from each section
    for section_name, coords in sections.items():
        segment_and_save_characters(image, coords, section_name, output_dir)

    print("Character segmentation and saving complete.")

if __name__ == "__main__":
    main()
