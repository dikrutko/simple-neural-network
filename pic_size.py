import os
from PIL import Image

filename = os.listdir("./Winter")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Winter"+"/"+obj)
   str_past_dir = "./Winter/"+obj
   folder = os.makedirs("./TWinter/{}".format(obj), exist_ok=True)
   str_new_dir = "./TWinter/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((100,100))
      new_im.save(str_new_dir+"/"+image)


