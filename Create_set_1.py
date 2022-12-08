import os
from PIL import Image

filenameTest = os.listdir("./Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Test"+"/"+obj)
   str_past_dir = "./Test/"+obj
   folder = os.makedirs("./Set_1/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_1/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Training"+"/"+obj)
   str_past_dir = "./Training/"+obj
   folder = os.makedirs("./Set_1/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_1/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)