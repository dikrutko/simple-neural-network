import os
from PIL import Image

filenameA = os.listdir("./Sets_for_224/animals")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameA:
   past_dir = os.listdir("./Sets_for_224/animals"+"/"+obj)
   str_past_dir = "./Sets_for_224/animals/"+obj
   folder = os.makedirs("./224/Set_1A/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_1A/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image) 

filenameIID = os.listdir("./Sets_for_224/Intel_Image_Dataset")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameIID:
   past_dir = os.listdir("./Sets_for_224/Intel_Image_Dataset"+"/"+obj)
   str_past_dir = "./Sets_for_224/Intel_Image_Dataset/"+obj
   folder = os.makedirs("./224/Set_1IID/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_1IID/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image) 

filenameLD = os.listdir("./Sets_for_224/Landscape_picture")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameLD:
   past_dir = os.listdir("./Sets_for_224/Landscape_picture"+"/"+obj)
   str_past_dir = "./Sets_for_224/Landscape_picture/"+obj
   folder = os.makedirs("./224/Set_1LP/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_1LP/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image)

filename = os.listdir("./Sets_for_224/Set_5")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Sets_for_224/Set_5"+"/"+obj)
   str_past_dir = "./Sets_for_224/Set_5/"+obj
   folder = os.makedirs("./224/Set_1/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_1/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image) 

filenameWA = os.listdir("./Sets_for_224/Wild_animals")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameWA:
   past_dir = os.listdir("./Sets_for_224/Wild_animals"+"/"+obj)
   str_past_dir = "./Sets_for_224/Wild_animals/"+obj
   folder = os.makedirs("./224/Set_1WA/{}".format(obj), exist_ok=True)
   str_new_dir = "./224/Set_1WA/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image)