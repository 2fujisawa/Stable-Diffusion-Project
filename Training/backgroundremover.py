import os
from rembg import remove
from PIL import Image

# Paths (Update these)
input_folder = "/Users/linusfujisawa/Desktop/pixar_style_output"  # Input folder with images - THIS IS THE FOLDER YOU CREATED AFTER RESIZING IT!
output_folder = "/Users/linusfujisawa/Desktop/pixar_style_dataset_no_bg"   # Output for no background

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all images in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        with open(input_path, "rb") as input_file:
            image_data = input_file.read()

        # Remove background
        output_image = remove(image_data)

        # Save the new image
        with open(output_path, "wb") as output_file:
            output_file.write(output_image)

        print(f"✅ Processed: {filename}")

print("🚀 Background removal complete!")