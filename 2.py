import os
from PIL import Image
from PIL import ImageFilter

#filename = os.listdir("./Winter")   ##Путь к папке для размещения оригинальных изображений

saple = Image.open('./2.JPG')
size = saple.size
width, height = saple.size
a = saple.crop((256,256,width-256,height-256))
w,h = a.size
a1 = a.resize((256,256))
#saple.show()
#a1 = saple.filter(ImageFilter.SMOOTH)
#a1 = saple.rotate(350); 
a1.show()
#a1.save('./Winter')