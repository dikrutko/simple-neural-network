import os
from PIL import Image
from PIL import ImageFilter

filename = os.listdir("./Winter")   ##Путь к папке для размещения оригинальных изображений

saple = Image.open('./Winter/elephant 100/IMG_0798.JPG')
#saple.show()
a1 = saple.filter(ImageFilter.SMOOTH)
a1.show()