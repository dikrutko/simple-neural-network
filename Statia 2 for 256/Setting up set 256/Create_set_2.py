import os
from PIL import Image

filenameTest = os.listdir("./Set_4/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Set_4/Test"+"/"+obj)
   str_past_dir = "./Set_4/Test/"+obj
   folder = os.makedirs("./256/Set_1/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filenameTraining = os.listdir("./Set_4/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Set_4/Training"+"/"+obj)
   str_past_dir = "./Set_4/Training/"+obj
   folder = os.makedirs("./256/Set_1/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./256/Set_1/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)
