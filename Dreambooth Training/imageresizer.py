import os
from PIL import Image

# Paths (Update these)
input_folder = "/Users/linusfujisawa/Desktop/PixarDataSetBefore"  # Original dataset folder
output_folder = "/Users/linusfujisawa/Desktop/pixar_style_dataset_resized"  # Resized output folder
target_size = (512, 512)  # Set your resize dimensions

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

            # Open image and resize
            with Image.open(input_path) as img:
                img = img.resize(target_size, Image.LANCZOS)  # Use LANCZOS filter for high-quality downsampling
                img.save(output_path)

            print(f"✅ Resized: {input_path} → {output_path}")