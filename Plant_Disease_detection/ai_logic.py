import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import io
import cnn_model  # Importing your model class
from plant_database import PLANT_DISEASE_INFO

# --- CONFIGURATION ---
MODEL_PATH = 'plant_disease_model_1_latest.pt'
NUM_CLASSES = 39

# 1. DEFINE CLASS LABELS (Must match CNN.py order exactly)
idx_to_classes = {
    0: 'Apple___Apple_scab', 1: 'Apple___Black_rot', 2: 'Apple___Cedar_apple_rust', 3: 'Apple___healthy',
    4: 'Background_without_leaves', 5: 'Blueberry___healthy', 6: 'Cherry___Powdery_mildew', 7: 'Cherry___healthy',
    8: 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 9: 'Corn___Common_rust', 10: 'Corn___Northern_Leaf_Blight', 11: 'Corn___healthy',
    12: 'Grape___Black_rot', 13: 'Grape___Esca_(Black_Measles)', 14: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 15: 'Grape___healthy',
    16: 'Orange___Haunglongbing_(Citrus_greening)', 17: 'Peach___Bacterial_spot', 18: 'Peach___healthy',
    19: 'Pepper,_bell___Bacterial_spot', 20: 'Pepper,_bell___healthy', 21: 'Potato___Early_blight', 22: 'Potato___Late_blight',
    23: 'Potato___healthy', 24: 'Raspberry___healthy', 25: 'Soybean___healthy', 26: 'Squash___Powdery_mildew',
    27: 'Strawberry___Leaf_scorch', 28: 'Strawberry___healthy', 29: 'Tomato___Bacterial_spot', 30: 'Tomato___Early_blight',
    31: 'Tomato___Late_blight', 32: 'Tomato___Leaf_Mold', 33: 'Tomato___Septoria_leaf_spot', 34: 'Tomato___Spider_mites Two-spotted_spider_mite',
    35: 'Tomato___Target_Spot', 36: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 37: 'Tomato___Tomato_mosaic_virus', 38: 'Tomato___healthy'
}

# 2. LOAD MODEL
device = torch.device("cpu")
try:
    model = cnn_model.CNN(NUM_CLASSES)
    # Load state dict
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()
    print(f"✅ PyTorch Model loaded from {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# 3. DEFINE TRANSFORMS (Must match training: Resize 255 -> CenterCrop 224 -> ToTensor)
transform = transforms.Compose([
    transforms.Resize(255),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

def get_plant_prediction(image_bytes):
    if not model:
        return {"error": "Model failed to load."}

    try:
        # Preprocess
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        tensor = transform(image).unsqueeze(0) # Add batch dimension

        # Predict
        with torch.no_grad():
            outputs = model(tensor)
            probabilities = F.softmax(outputs, dim=1)
            confidence, predicted_idx = torch.max(probabilities, 1)
            
            idx = predicted_idx.item()
            conf = confidence.item()

        predicted_class_key = idx_to_classes.get(idx, "default")
        
        # Get Details
        disease_details = PLANT_DISEASE_INFO.get(predicted_class_key, PLANT_DISEASE_INFO['default']).copy()

        return {
            "prediction": disease_details['name'],
            "original_class": predicted_class_key,
            "confidence": f"{conf * 100:.2f}%",
            "details": disease_details
        }

    except Exception as e:
        return {"error": str(e)}