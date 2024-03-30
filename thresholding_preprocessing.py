import cv2
import os

# Path to the image folder and where you want to save thresholded images
image_folder = "C:/Users/Jimi2/OneDrive/Desktop/Test output/"
output_folder = "C:/Users/Jimi2/OneDrive/Desktop/threshold"

# Loop through images
for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Read image in grayscale

    # Apply thresholding (example with simple threshold)
    _, thresholded = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Save thresholded images
    output_path = os.path.join(output_folder, f'healthy_{img_name}')
    cv2.imwrite(output_path, thresholded)