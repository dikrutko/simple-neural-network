import os
from PIL import Image

filenameTest = os.listdir("./Wild animals/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Wild animals/Test"+"/"+obj)
   str_past_dir = "./Wild animals/Test/"+obj
   folder = os.makedirs("./160/Set_1WA/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1WA/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Wild animals/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Wild animals/Training"+"/"+obj)
   str_past_dir = "./Wild animals/Training/"+obj
   folder = os.makedirs("./160/Set_1WA/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1WA/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./Wild animals/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Wild animals/Valid"+"/"+obj)
   str_past_dir = "./Wild animals/Valid/"+obj
   folder = os.makedirs("./160/Set_1WA/Valid/{}".format(obj), exist_ok=True)
   str_new_dir = "./160/Set_1WA/Valid/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((160,160))
      new_im.save(str_new_dir+"/"+image)