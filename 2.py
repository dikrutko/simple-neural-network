import os
from PIL import Image
from PIL import ImageFilter

filename = os.listdir("./Winter")   ##Путь к папке для размещения оригинальных изображений

saple = Image.open('./Winter/rock_grandfather 144/IMG_E8791.JPG')
#saple.show()
#a1 = saple.filter(ImageFilter.SMOOTH)
a1 = saple.rotate(350); 
a1.show()
#a1.save('./Winter')