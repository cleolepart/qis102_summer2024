import cv2
import os

def draw_bounding_boxes(image, sections):
    """
    Draw bounding boxes on the image to verify the sections.
    Args:
    - image: The preprocessed image.
    - sections: Dictionary containing section names and their coordinates (x, y, w, h).
    """
    for section_name, (x, y, w, h) in sections.items():
        # Draw a rectangle around the section
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Put the section name on the top-left corner of the rectangle
        cv2.putText(image, section_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Display the image with bounding boxes
    cv2.imshow('Sections with Bounding Boxes', image)
    print("Press 'q' or 'Esc' to close the window")

    # Wait for a specific key press to close the window
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' key or 'Esc' key to exit
            break

    # Close the OpenCV window
    cv2.destroyAllWindows()




# Global variables
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1  # Initial position of the rectangle
rectangles = []  # List to store the rectangles

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, image, rectangles

    # If the left mouse button is pressed, record the starting position
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # If the mouse is moved with the button pressed, draw the rectangle
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = image.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (255, 0, 0), 2)
            cv2.imshow('Image', img_copy)

    # When the left mouse button is released, finalize the rectangle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangles.append((ix, iy, x - ix, y - iy))
        cv2.rectangle(image, (ix, iy), (x, y), (255, 0, 0), 2)
        cv2.imshow('Image', image)

def main():
    global image

    image_directory = 'Session 00 - Rosetta Stone/'
    # Path to the preprocessed image
    image_path = os.path.join(image_directory, 'thresholded_champollion_hieroglyphs.jpg')

    # Load the preprocessed image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Define the sections of the image (x, y, width, height)
    sections = {
        "Greek_Letters": (50, 100, 300, 600),
        "Demotic_Signs": (400, 100, 300, 600),
        "Hieroglyphic_Signs": (750, 100, 800, 600),
    }

    # Draw bounding boxes and verify sections
    draw_bounding_boxes(image, sections)

    # Create a window and set the mouse callback function
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_rectangle)

    # Display the image
    cv2.imshow('Image', image)
    print("Draw rectangles by dragging with the left mouse button. Press 'q' to finish.")

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 'q' key to exit
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Print the coordinates of the rectangles
    for i, rect in enumerate(rectangles):
        print(f"Section {i + 1}: (x={rect[0]}, y={rect[1]}, width={rect[2]}, height={rect[3]})")

if __name__ == "__main__":
    main()

