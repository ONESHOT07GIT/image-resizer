from PIL import Image
import os

UPLOAD_FOLDER = "uploads"
RESIZED_FOLDER = "resized"
SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]

def resize_images(image_path):
    resized_images = []
    os.makedirs(RESIZED_FOLDER, exist_ok=True)
    
    for size in SIZES:
        img = Image.open(image_path)
        img = img.resize(size)
        resized_path = os.path.join(RESIZED_FOLDER, f"{size[0]}x{size[1]}_{os.path.basename(image_path)}")
        img.save(resized_path)
        resized_images.append(resized_path)
    
    return resized_images
