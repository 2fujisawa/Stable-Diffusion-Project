### BASIC LAYOUT OF STABLE DIFFUSION UI (Automatic1111)

# Stable Diffusion Checkpoint
The basic model selector which you can bring in your own custom model or bring in models created by others.

# text2img
Create images just using text prompts.

# img2img
Create images using other images and text prompts.

# Extras
Primarily used for image processing including upscaling (Improve resolution and details).

# PNG Info
Used to extract metadata from images that were generated using Stable Diffusion. When you generate an image, the settings (prompts, model, seed, etc.) are embedded in the PNG file itself. This tab allows you to read and reuse those settings.

# Checkpoint Merger
Combines models/checkpoints up to 3 and create a merged model.

# Train
Used for fine-tuning and training custom models, such as:
Ex. LoRA (Low-Rank Adaptation), Textual Inversion, DreamBooth, Hypernetworks.

# Setting
Adjust the basic setting in the stable diffusion provided.

# Extension
Extensions you can turn on, off, add, remove, from stable diffusion.

### GENERATION TAB

# Sampling Method
How to determine how an image is refined from random noise over multiple steps. Each method has a unique way of estimating and reducing noise, leading to different speeds, quality levels, and styles of output.

- **DPM++ 2M**: A modified version of DPM++ that balances speed and quality. Good for general use.
- **DPM++ SDE**: Uses stochastic differential equations (SDE) for better variance control. Great for fine details but slower.

# Schedule Type
How noise is removed over the sampling steps. Different schedules can affect the sharpness, smoothness, and coherence of the final image.

- **Uniform**:
  - Applies equal noise reduction across all steps.
  - Results in consistent but sometimes blurry images.
  - Best for: Basic testing or low-step generations.

- **Karras**:
  - Produces sharp, detailed images with fewer steps.
  - Recommended for: High-quality generations with DPM++ samplers.
  - Best for: General use, portraits, fine details, realistic shading.

- **Exponential**:
  - Generates softer, smoother images but may lose fine details.
  - Recommended for: Dreamy, soft-focus styles, artistic effects.
  - Best for: Cartoon, anime, or painterly effects.

- **Polyexponential**:
  - Similar to Exponential but more aggressive in fine-tuning.
  - Tries to balance noise removal between early and late stages.
  - Best for: Complex images with fine details.

- **SGM Uniform** (⭐️):
  - A more structured approach to uniform scheduling.
  - Ensures a consistent denoising rate with a slight bias towards final steps.
  - Best for: Sharp details while maintaining uniformity.

- **KL Optimal**:
  - A schedule optimized for fast sampling with minimal loss in quality.
  - Designed for efficient image generation with lower steps.
  - Best for: Fast generations while maintaining quality.

- **Align Your Steps** (⭐️):
  - Adjusts denoising dynamically based on sampling steps.
  - Best for: Long-step generations where consistency matters with the original photo.

- **Simple** (⭐️):
  - A straightforward linear approach to noise reduction.
  - Often results in less detailed but balanced outputs.
  - Best for: Users who want a no-frills, predictable output.

- **Normal** (⭐️):
  - A mix of linear and exponential noise removal.
  - Slightly more detail than Simple but not as refined as Karras.
  - Best for: Standard results without excessive tuning.

- **DDIM**:
  - Non-Markovian diffusion model that enables faster image generation.
  - Reduces noise very quickly, making it efficient for low-step renders.
  - Best for: Speed and efficiency (but slightly reduced detail).

- **Beta** (⭐️ Newer, but matches the model stylization even with low denoising strength):
  - A custom schedule that fine-tunes noise reduction based on beta distribution.
  - Best for: Experimental settings, but not widely used.

# Sampling Steps
Control the iteration/cycle count for the AI to refine the image. Higher count = better image quality but slow processing speed. Low count = Less image quality but better processing.

- **IMPORTANT**: MORE STEPS DOES NOT ALWAYS MEAN BETTER AFTER THE 30-50 STEP MARK A LOT OF THE QUALITY IMPROVEMENTS SLOW DOWN.

# Refiner (For Stable Diffusion XL)
Designed to improve image quality by enhancing finer details while the image is being generated. Improves in details, textures, and sharpness.

# IMPORTANT FOR VRAM USAGE
- **Batch Count**: Defines the number of times the model will run the generation process. Doesn't increase VRAM usage, generates multiple images but one at a time.
- **Batch Size**: Determines how many images are generated simultaneously in one go. Uses more VRAM as the model generates multiple images at once all together.

# CFG Scale
Accuracy with how much the AI is supposed to follow your text prompt. "Strictness" for your model.

- **Low (1-5)**: AI is creative, doesn't strictly follow your prompt/less predictable output. Good for abstract, dreamy, or artistic images.
- **Medium (6-10)**: Balances creativity and prompt accuracy. Best for realistic and well-structured images.
- **High (11-20)**: AI follows prompt very strictly, causes oversharpening and unnatural distortions.

# Denoising Strength
Accuracy with the original picture provided with img2img.

- **Low (0.1 - 0.3)**: Minimal changes to the images, keeps most of the original details intact.
- **Medium (0.4 - 0.7)**: Moderate transformation to the image, adds more creativity but still maintains some original structure.
- **High (0.8 - 1.0)**: Lots of AI freedom and the image might not resemble the original much, however, the composition is kept.

# Seed
A random number that determines how an image is generated. Acts as a starting point for the AI to generate noise, which then gets refined into an image. Maintains pose, layout, composition. 🚨 Needs more testing.

- **Fixed Seed**: Generates the same image every time with the same settings.
- **Random Seed (-1)**: Generates a new image every time.

### What the Seed Controls:
- **Noise Pattern**: The initial random noise that Stable Diffusion starts with.
- **Base Structure**: The overall composition and arrangement of elements in the image.
- **Repeatability**: If you use the same seed + exact same settings, you get the same image.