from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load the trained model
model = tf.keras.models.load_model('fashion_mnist_cnn_model.h5')

# Define the FastAPI app
app = FastAPI()

# Class names for the Fashion MNIST dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 
               'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Define the prediction endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to the required input shape
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=-1)  # Add channel dimension
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(image)
    predicted_class = class_names[np.argmax(predictions)]
    
    return JSONResponse(content={"predicted_class": predicted_class})

# Run the FastAPI app (use `uvicorn app:app --reload` to run)
