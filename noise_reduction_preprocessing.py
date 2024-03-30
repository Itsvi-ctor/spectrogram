import cv2
import os

# Define paths
# code_file_path = r'C:\Users\Jimi2\Documents\preprocessing\Noise Reduction'
# image_folder_path = r'C:\Users\Jimi2\Documents\Test\Healthy_test'
image_folder_path = "C:/Users/Jimi2/OneDrive/Desktop/Test output/"
# output_folder_path = r'C:\Users\Jimi2\Documents\preprocessing\Noise Reduction\NoiseReduced_healthy_test'
output_folder_path="C:/Users/Jimi2/OneDrive/Desktop/threshold"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through images in the folder
for img_name in os.listdir(image_folder_path):
    img_path = os.path.join(image_folder_path, img_name)
    
    # Read the image
    img = cv2.imread(img_path)
    
    # Apply noise reduction (denoising)
    denoised_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
    
    # Save the denoised image with the title "healthy" in the output folder
    output_img_path = os.path.join(output_folder_path, f'healthy_{img_name}')
    cv2.imwrite(output_img_path, denoised_img)