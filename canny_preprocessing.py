import cv2
import os

# Define paths
image_folder_path = "C:/Users/Jimi2/OneDrive/Desktop/Test output/"
output_folder_path = "C:/Users/Jimi2/OneDrive/Desktop/canny/"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through images in the folder
for img_name in os.listdir(image_folder_path):
    img_path = os.path.join(image_folder_path, img_name)
    
    # Read the image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)  # Adjust the thresholds as needed
    
    # Save the Canny edges image
    output_img_path = os.path.join(output_folder_path, f'canny_{img_name}')
    cv2.imwrite(output_img_path, edges)
