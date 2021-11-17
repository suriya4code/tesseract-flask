from flask import Flask
from flask_restx import Resource, Api
from werkzeug.datastructures import FileStorage
import io
import cv2
import numpy as np
import pytesseract

app = Flask(__name__)
api = Api(app)

upload_parser = api.parser()
upload_parser.add_argument('file',location='files',type=FileStorage)

def read_image(img):
    pytesseract.pytesseract.tesseract_cmd =     './.apt/usr/bin/tesseract'
    content = pytesseract.image_to_string(img)
    return content



@api.route('/predict/')
@api.expect(upload_parser)
class Tesseract(Resource):
    def get(self):
        print("reached get tesseract")
        return "predicted"
    
    def post(self):
        print("file received")
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        image_stream = io.BytesIO(uploaded_file.read())
        image_stream.seek(0)
        filebytes = np.asarray(bytearray(image_stream.read()),dtype=np.uint8)
        frame = cv2.imdecode(filebytes, cv2.IMREAD_COLOR)
        label = read_image(frame)
        return label

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 