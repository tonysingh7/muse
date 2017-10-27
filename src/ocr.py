#import packages
from PIL import Image
import pytesseract as pyt

filedir = "/home/echo/Repos/muse/images/text.png"
text = pyt.image_to_string(Image.open(filedir))
print (text)
