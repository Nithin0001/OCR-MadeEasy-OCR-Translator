# for translation
from googletrans import Translator
# for ocr
import pytesseract
# for image opening
from PIL import Image

t = Translator()
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'

r = ""
translated = ""


# tesseract api call function
def img_extract(path, lan):
    img = Image.open(path)
    global r
    r = str(pytesseract.image_to_string(img, lang=lan))
    return r


# google api call function
def translate(from_ln, to_ln, re):
    global translated
    translated = t.translate(re, src=from_ln, dest=to_ln)
    return translated.text
