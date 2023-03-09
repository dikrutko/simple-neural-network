import os
from PIL import Image

filenameTest = os.listdir("./Sets for 160/animals/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/animals/Test"+"/"+obj)
   str_past_dir = "./Sets for 160/animals/Test/"+obj
   folder = os.makedirs("./256/Set_1A/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1A/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Sets for 160/animals/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/animals/Training"+"/"+obj)
   str_past_dir = "./Sets for 160/animals/Training/"+obj
   folder = os.makedirs("./256/Set_1A/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1A/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./Sets for 160/animals/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/animals/Valid"+"/"+obj)
   str_past_dir = "./Sets for 160/animals/Valid/"+obj
   folder = os.makedirs("./256/Set_1A/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1A/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)