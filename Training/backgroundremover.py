import os
from rembg import remove
from PIL import Image

# Paths (Update these)
input_folder = "/Users/linusfujisawa/Desktop/pixar_style_dataset_resized"  # Your resized dataset folder
output_folder = "/Users/linusfujisawa/Desktop/pixar_style_dataset_no_bg"  # Output for no background

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Walk through all subfolders and process images
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            input_path = os.path.join(root, filename)

            # Create the same subfolder structure in output
            relative_path = os.path.relpath(root, input_folder)
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)

            output_path = os.path.join(output_subfolder, filename)

            # Open the image
            with open(input_path, "rb") as input_file:
                image_data = input_file.read()

            # Remove background
            output_image = remove(image_data)

            # Save the new image
            with open(output_path, "wb") as output_file:
                output_file.write(output_image)

            print(f"✅ Background Removed: {input_path} → {output_path}")