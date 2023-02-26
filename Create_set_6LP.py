import os
from PIL import Image

filenameTest = os.listdir("./Landscape_picture/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Landscape_picture/Test"+"/"+obj)
   str_past_dir = "./Landscape_picture/Test/"+obj
   folder = os.makedirs("./Set_1LP/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_1LP/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Landscape_picture/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Landscape_picture/Training"+"/"+obj)
   str_past_dir = "./Landscape_picture/Training/"+obj
   folder = os.makedirs("./Set_1LP/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_1LP/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./Landscape_picture/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Landscape_picture/Valid"+"/"+obj)
   str_past_dir = "./Landscape_picture/Valid/"+obj
   folder = os.makedirs("./Set_1LP/Valid/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_1LP/Valid/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)