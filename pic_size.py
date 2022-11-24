import os
from PIL import Image

filename = os.listdir("./Winter")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Winter"+"/"+obj)
   str_past_dir = "./Winter/"+obj
   folder = os.makedirs("./TWinter/{}".format(obj), exist_ok=True)
   str_new_dir = "./TWinter/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((100,100))
      new_im.save(str_new_dir+"/"+image)




""" filename = os.listdir("./Training/elephant")   ##Путь к папке для размещения оригинальных изображений
base_dir = r"./Training/elephant/"    ## Путь к папке для размещения оригинальных изображений
new_dir = r"./Size_new/Training/elephant/"    ## Путь к файлу нового изображения

for img in filename:
    image = Image.open(base_dir + img)
    size_m, size_n = image.size
    #size_m = int(size_m / 2)
    #size_n = int(size_n / 2)
    #image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
    image_size = image.resize((100, 100), Image.NEAREST)   
 # ## Самая важная функция находится здесь.Когда вам это нужно, вам нужно только изменить число после изменения размера в этой строке, закомментировать первые три строки и использовать эту строку.
    image_size.save(new_dir + img) """