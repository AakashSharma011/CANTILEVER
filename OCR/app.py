from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Set Tesseract executable path (Change this to your installed location)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # <-- Change this path if needed

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    image_path = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            image_path = file_path
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)
    return render_template('index.html', extracted_text=extracted_text, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
