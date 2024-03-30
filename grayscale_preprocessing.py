import cv2
import os

# Define paths
image_folder_path = "C:/Users/Jimi2/OneDrive/Desktop/Test output/"
output_folder_path = "C:/Users/Jimi2/OneDrive/Desktop/grayscale"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through images in the folder
for img_name in os.listdir(image_folder_path):
    img_path = os.path.join(image_folder_path, img_name)
    
    # Read the image
    img = cv2.imread(img_path)
    
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image with the title "gray_" in the output folder
    output_img_path = os.path.join(output_folder_path, f'gray_{img_name}')
    cv2.imwrite(output_img_path, gray_img)
