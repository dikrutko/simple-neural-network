import os
from PIL import Image

filename2Test = os.listdir("./Set_1/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filename2Test:
   past_dir = os.listdir("./Set_1/Test"+"/"+obj)
   str_past_dir = "./Set_1/Test/"+obj
   folder = os.makedirs("./224/Set_2/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_2/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image) 

filename2Training = os.listdir("./Set_1/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filename2Training:
   past_dir = os.listdir("./Set_1/Training"+"/"+obj)
   str_past_dir = "./Set_1/Training/"+obj
   folder = os.makedirs("./224/Set_2/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_2/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image) 