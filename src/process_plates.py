import re
import numpy
import pytesseract
import open_cv as cv
from PIL import Image

time_to_wait_ms = 5000
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
allowed_plates = ['PLA0000', 'EWK7037']
recognized_image = 'recognized.jpg'
images_paths = [
    '../images/plate.JPG',
    '../images/plate1.jpg',
    '../images/plate2.jpg',
    '../images/plate3.jpg',
    '../images/plate4.jpg'
]

def get_custom_config():
    return r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'

def image_to_string(custom_config):
    return pytesseract.image_to_string(Image.open(recognized_image), config=custom_config)

def apply_regex(ex):
    return re.sub(r'[-|\s“"—— \n_]', "", ex)

def recognize_image():
    custom_config = get_custom_config()
    recognized_plate = image_to_string(custom_config)
    recognized_plate = apply_regex(recognized_plate)
    print_decision(recognized_plate, allowed_plates)

def print_decision(recon_plate, allow_plate):
    print(recon_plate)
    if recon_plate in allow_plate:
        print('Plate allowed')
    else:
        print('Plate not allowed')
    
def open_image_and_recognize(image_path):
    image = cv.loades_image(image_path)
    gray_scale = cv.show_image(image, image_path)
    cv.saves_image(recognized_image, gray_scale)
    recognize_image()
    cv.wai_time(time_to_wait_ms)

def process_image_plates():
    for i in range (len(images_paths)):
        open_image_and_recognize(images_paths[i])

process_image_plates()