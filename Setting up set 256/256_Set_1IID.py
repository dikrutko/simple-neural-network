import os
from PIL import Image

filenameTest = os.listdir("./Sets for 160/Intel Image Dataset/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/Intel Image Dataset/Test"+"/"+obj)
   str_past_dir = "./Sets for 160/Intel Image Dataset/Test/"+obj
   folder = os.makedirs("./256/Set_1IID/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1IID/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Sets for 160/Intel Image Dataset/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/Intel Image Dataset/Training"+"/"+obj)
   str_past_dir = "./Sets for 160/Intel Image Dataset/Training/"+obj
   folder = os.makedirs("./256/Set_1IID/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1IID/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameValid = os.listdir("./Sets for 160/Intel Image Dataset/Valid")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Sets for 160/Intel Image Dataset/Valid"+"/"+obj)
   str_past_dir = "./Sets for 160/Intel Image Dataset/Valid/"+obj
   folder = os.makedirs("./256/Set_1IID/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1IID/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)