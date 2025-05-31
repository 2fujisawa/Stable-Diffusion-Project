# 🛠️ Training Process

Originally, I attempted to run training locally, but since I was using a **Mac** (which lacks NVIDIA GPU and CUDA support), I wasn’t able to run **Stable Diffusion training or DreamBooth locally**.  

To overcome this:  
✅ I used **Google Colab** ☁️ to perform the training and fine-tuning in the cloud.  
✅ After training, I transferred the **trained model** to my **local NVIDIA-based PC** 🖥️ and ran it using **Automatic1111 Web UI** for optimized local image generation.

---

## ⚠️ Hardware Requirements

🚫 **Important Note:**  
- **Mac systems (Intel or M1/M2/M3)** are not compatible for local Stable Diffusion training or for running **Automatic1111 Web UI**.  
- Requires a system with an **NVIDIA GPU** (CUDA support) to run both training and optimized local inference.  
- In this project, I used:  
  - **Google Colab** ☁️ for training  
  - **NVIDIA GPU PC** 🖥️ for local inference with **Automatic1111 Web UI**

---

## 🚀 How DreamBooth Works

DreamBooth fine-tunes an existing model (such as **Stable Diffusion 1.5 or 3.5**) by:

1️⃣ **Associating a Unique Token** 🏷️  
👉 You assign a new identifier (token) that doesn't already exist in the model.  
👉 Example: `"sks_pixarstyle"` — this token gets embedded in the model and is used in prompts after training.  

2️⃣ **Teaching the Model New Visual Features** 🖌️  
👉 You provide a small image dataset (e.g. Pixar-style artwork).  
👉 The model learns **artistic traits** like brush strokes, colors, lighting, and composition.  

3️⃣ **Blending New Knowledge Into Stable Diffusion** 🔄  
👉 DreamBooth **augments** the model — it doesn't replace existing knowledge.  
👉 After training, you can use your token (ex: `"sks_pixarstyle"`) to apply the style to any prompt.

4️⃣ **Training Parameters** ⚙️  
👉 DreamBooth fine-tunes **specific layers** of the model — not the entire model — to avoid overfitting and preserve general capabilities.

---

# ⚙️ Training Parameters — Explained

### 🖥️ Settings

**1️⃣ Model**  
- Selects your training model.  
- The output is an **incremental checkpoint** of your fine-tuning progress (not a full `.ckpt` until exported).  

---

**2️⃣ Concepts**  
Defines what your model is learning — helps it associate the **new style** (Pixar-inspired) with your token:

- **Instance Images** 🖼️ → Path to your training image folder.  
- **Prompt** ✏️ → Describes what your images represent (ex: `"a Pixar-style pet"`).  
- **Instance Token** 🏷️ → The **keyword** that activates your trained style (ex: `"sks_pixarstyle"`).  
- **Class Token** 🏷️ → Optional — used for training **specific objects or people** (prevents overfitting).  

🚨 **Concept Boxes** (Concept 1–4) → Allow you to train **multiple styles** in one session (ex: Pixar, Watercolor, Anime).  

---

**3️⃣ Class Images** 🐕 →  
- Used when training **specific objects** (ex: dog breeds).  
- Helps the model **differentiate between object features** and style.  
- Useful for **object-focused training** — not needed for pure stylization.

---

**4️⃣ Sample Images** 🧪 →  
- Automatically generated **during training** to monitor progress.  
- Helps check for:  
    - **Overfitting** 🔥 (too much memorization)  
    - **Underfitting** 🧊 (not learning enough)  
- Lets you evaluate model performance in **real-time**.

---

**5️⃣ Parameters** ⚙️ →  
Control how the model learns:  
✅ Learning rate  
✅ Training steps  
✅ Scheduler  
✅ Regularization  

Proper tuning ensures your model **learns the target style** (Pixar) without overfitting.