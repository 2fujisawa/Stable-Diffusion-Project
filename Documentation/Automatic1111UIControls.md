# 🖥️ Basic Layout of Stable Diffusion UI (Automatic1111)

---

## 🗂️ Stable Diffusion Checkpoint

🔸 The main **model selector** — lets you load a **custom model** (your trained DreamBooth model) or models created by others.

---

## 🖼️ Core Tabs

### ✏️ **text2img**  
👉 Generate images **from text prompts**.

### 🖼️ **img2img**  
👉 Generate images **from an existing image + text prompts** (useful for refining or transforming images).

### 🛠️ **Extras**  
👉 Tools for **image processing**, including:
- **Upscaling** 🔍 (improve resolution & detail)
- Other post-processing tools.

### 📝 **PNG Info**  
👉 Extract metadata from generated images:
- Embedded info includes **prompt**, **model used**, **seed**, **settings**.  
- Lets you **reproduce or fine-tune** previous generations.

### 🔀 **Checkpoint Merger**  
👉 Merge up to **3 models/checkpoints** into a new combined model.

### 🧑‍🏫 **Train**  
👉 Tools for **fine-tuning and training**:
- **LoRA (Low-Rank Adaptation)** 🧩  
- **Textual Inversion** 🏷️  
- **DreamBooth** 🐾  
- **Hypernetworks** 🔄  

### ⚙️ **Settings**  
👉 Adjust core **Stable Diffusion settings**.

### 🧩 **Extensions**  
👉 Enable/disable **extensions**.  
👉 Add or remove new features to Stable Diffusion.

---

# 🎛️ Generation Tab

---

## 🌀 **Sampling Method**

Controls **how the image is refined from noise** over multiple steps.  
Different methods balance **speed**, **quality**, and **style**:

- **DPM++ 2M** ⚖️ — Good speed/quality balance.
- **DPM++ SDE** 🔍 — Finer detail (slower).
- **DDIM** ⚡ — Fast generation (lower detail).
- And many more (see below ↓ for Scheduling).

---

## ⏳ **Schedule Type**

Controls **how noise is removed** at each step:

- **Uniform** ➡️ Basic consistent reduction.
- **Karras** 🌟 Sharp, detailed results (best general choice).
- **Exponential** ✨ Softer, dreamy images.
- **Polyexponential** 🎨 Fine-tuned complex images.
- **SGM Uniform** ⭐ Sharp + uniform.
- **KL Optimal** ⚡ Fast + quality.
- **Align Your Steps** 🧭 Adaptive noise removal.
- **Simple** ➡️ Linear, predictable output.
- **Normal** ➡️ Balanced noise removal.
- **Beta** 🧪 Experimental.
- **DDIM** ⚡ Fast, efficient.

---

## 🪜 **Sampling Steps**

Controls **how many steps** the model takes to refine an image:

- More steps → **higher quality** (to a point).
- ⚠️ After **30-50 steps**, quality improvements slow down.

---

## 🖌️ **Refiner** (for SDXL models)

Improves **fine details** during generation — adds sharpness & texture.

---

## 🔄 **Batch Count**

Number of **generation runs** (how many times to run the model).  
- Doesn’t affect VRAM — runs **one at a time**.

---

## 🖼️ **Batch Size**

How many images to generate **at once**:  
- **Higher batch size = more VRAM usage**.  
- Generates **multiple images simultaneously**.

---

## 🎛️ **CFG Scale** (Classifier-Free Guidance)

Controls **how strictly the model follows the text prompt**:

- **Low (1-5)** → More creative 🎨, loose interpretation.
- **Medium (6-10)** → Balanced, realistic results.
- **High (11-20)** → Very strict 📏, can cause artifacts if too high.

---

## 🔁 **Denoising Strength** (for img2img)

Controls how much the model **changes the original image**:

- **Low (0.1 - 0.3)** → Minor edits 🖼️.
- **Medium (0.4 - 0.7)** → Balanced transformation.
- **High (0.8 - 1.0)** → Major changes 🎨.

---

## 🎲 **Seed**

The **random seed** determines **how noise is initialized**:

- **Fixed Seed** → Same output each time (reproducible).  
- **Random Seed (-1)** → New image each time.

What the seed controls:

- **Noise Pattern** 🎲.
- **Base Composition** 🖼️.
- **Repeatability** 🔄 (important for controlled generation).

---

# ⭐ Summary

**Automatic1111 Web UI** provides a **powerful, flexible interface** for:

✅ Loading custom models  
✅ Generating images (text2img, img2img)  
✅ Fine-tuning and merging models  
✅ Controlling generation parameters for **style, quality, and repeatability**  

---
