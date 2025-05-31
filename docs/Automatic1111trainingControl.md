# For the training we will be using Dreambooth within Automatic1111 as a extension

## DreamBooth is a fine-tuning method for Stable Diffusion that allows you to train a model to recognize new styles, objects, or people using a small dataset. Unlike general AI training, which requires millions of images, DreamBooth allows you to train with as little as 5-20 images.

Fine tunes an existing model like stable diffusion 1.5 by 

1. Associating a Unique Token (sks_pixarstyle)
	•	You give DreamBooth a new identifier (token) that doesn’t already exist in the model.

        THIS IS A CUSTOM KEYWORD THAT GETS EMBEDDED INTO THE MODEL AS YOU WILL USE THIS IN PROMPTS TO FOLLOW THE STYLE AFTER TRAINING
	•	Example: "sks_pixarstyle" (to represent Pixar-style brushwork). your custom keyword that gets embedded in the model.

2.	Teaching the Model New Visual Features
	•	You provide a small dataset of images (e.g., your Pixar-style dataset).
	•	The model learns artistic traits like brush strokes, colors, and lighting from these images.

3.	Blending the New Knowledge Into Stable Diffusion
	•	Instead of replacing what the model already knows, DreamBooth integrates your dataset into existing AI knowledge.
	•	This means you can now use sks_pixarstyle in prompts to generate any subject in the Pixar style.

4. Training Parameters
	•	DreamBooth uses a pre-trained model (like Stable Diffusion 1.5) as the base.
	•	It fine-tunes specific parts of the model (not the whole thing) to memorize your dataset without overwriting.


# Training Parameters control explanations
## Setting
1. Model - This portion allows you select and create your own training model. This is not the full complete .ckpt file its just going to be the precheckpoint state where it saves your training process

2. Concepts -  defines what your model is learning and helps it associate a new concept (Pixar-style) with a specific token (sks_pixarstyle).

    Instance Images(Main training data) - This is the path to your dataset folder/directory containing your training images.

        Prompt - The Prompt field describes what your images represent. This is what the AI associates with your instance token (sks_pixarstyle).

        Instance Token - This is the keyword that activates the trained style after training.

        Class Token - A Class Token is mainly used when training specific objects or people, not styles. Class Tokens are for preventing overfitting on a specific object

        🚨 The four concept boxes in DreamBooth (Concept 1, Concept 2, Concept 3, Concept 4) exist to allow training multiple concepts in a single session. Ex.Watercolor and Anime
    

    Class Images(Training to regularize specifc objects or people) - It is used to compare and contrast specifc objects. Use this when you will be comparing specifc dog breeds instead of focusing more on the texture and stylization. 

	Sample Images(Used to monitor training progress in real time) - Check for problems like overfitting (too much memorization) or underfitting (not learning enough). - Generates test images during training so you can see the models progress

3. Parameters - Controls how your model learns. Setting these corretly will help you AI learn the Pixar style without overfitting'
	