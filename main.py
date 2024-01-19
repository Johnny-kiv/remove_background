from rembg import remove
from PIL import Image

path = "img.jpg"
opath = "out.png"

input = Image.open(path)
output = remove(input)
output.save(opath)