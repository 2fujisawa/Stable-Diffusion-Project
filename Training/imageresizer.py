from PIL import Image
import os

# Set input & output folder
input_folder = "/Users/linusfujisawa/Desktop/pixar_style_dataset"
output_folder = "/Users/linusfujisawa/Desktop/pixar_style_output"
size = (512, 512)  # Change to (1024, 1024) for SDXL

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through images and resize
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize(size, Image.LANCZOS)  # High-quality resize
        img.save(os.path.join(output_folder, filename))

print("✅ All images resized successfully!")