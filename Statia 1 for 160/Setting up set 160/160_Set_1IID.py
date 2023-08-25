import os
from PIL import Image

filenameTest = os.listdir("./Intel Image Dataset/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Intel Image Dataset/Test"+"/"+obj)
   str_past_dir = "./Intel Image Dataset/Test/"+obj
   folder = os.makedirs("./160/Set_1IID/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1IID/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Intel Image Dataset/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Intel Image Dataset/Training"+"/"+obj)
   str_past_dir = "./Intel Image Dataset/Training/"+obj
   folder = os.makedirs("./160/Set_1IID/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1IID/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./Intel Image Dataset/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Intel Image Dataset/Valid"+"/"+obj)
   str_past_dir = "./Intel Image Dataset/Valid/"+obj
   folder = os.makedirs("./160/Set_1IID/Valid/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1IID/Valid/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)