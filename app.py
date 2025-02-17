from flask import Flask, request, render_template
import os
from image_utils import resize_images
from twitter_utils import post_images_to_twitter

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            resized_images = resize_images(filepath)
            post_images_to_twitter(resized_images)

            return "Images resized and posted to Twitter!"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
