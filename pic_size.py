import os
from PIL import Image


filename = os.listdir("./Training/elephant")   ##Путь к папке для размещения оригинальных изображений
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
    image_size.save(new_dir + img)