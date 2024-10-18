from PIL import Image
import os
import cv2 as cv
import numpy as np

def convert_to_grayscale_and_save(img_path, output_dir):
    # Open the image and convert it to grayscale
    grayscale_img = Image.open(img_path).convert('L')

    # Create the output path for saving the grayscale image
    output_path = os.path.join(output_dir, os.path.basename(img_path))

    # Save the grayscale image using OpenCV
    cv.imwrite(output_path, np.array(grayscale_img))
    print(f"Processed and saved: {os.path.basename(img_path)}")

# Example usage
input_dir = "s2"
output_img_dir = 's1'

# Ensure the output directory exists
if not os.path.exists(output_img_dir):
    os.makedirs(output_img_dir)

# Loop through all images in the input directory
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        convert_to_grayscale_and_save(file_path, output_img_dir)
