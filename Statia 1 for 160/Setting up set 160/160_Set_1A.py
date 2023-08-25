import os
from PIL import Image

filenameTest = os.listdir("./animals/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./animals/Test"+"/"+obj)
   str_past_dir = "./animals/Test/"+obj
   folder = os.makedirs("./160/Set_1A/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1A/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./animals/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./animals/Training"+"/"+obj)
   str_past_dir = "./animals/Training/"+obj
   folder = os.makedirs("./160/Set_1A/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1A/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./animals/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./animals/Valid"+"/"+obj)
   str_past_dir = "./animals/Valid/"+obj
   folder = os.makedirs("./160/Set_1A/Valid/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1A/Valid/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)