import os
from PIL import Image
from PIL import ImageFilter

filename = os.listdir("./Size_new_new/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Size_new_new/Training"+"/"+obj)
   str_past_dir = "./Size_new_new/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      
      det = im.filter(ImageFilter.DETAIL)
      det.save(str_past_dir+"/"+"z1_det_"+image)
      
      det = im.filter(ImageFilter.SMOOTH)
      det.save(str_past_dir+"/"+"z2_smooth_"+image)
      
print("Применен фильтр улучшения деталей, который сделает детали более очевидными")  
print("Применен плавный фильтр")

for obj in filename:
   past_dir = os.listdir("./Size_new_new/Training"+"/"+obj)
   str_past_dir = "./Size_new_new/Training/"+obj
   #folder = os.makedirs("./TWinter/{}".format(obj), exist_ok=True)
   #str_new_dir = "./TWinter/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      rot10 = im.rotate(10)
      rot10.save(str_past_dir+"/"+"z3_rot10_"+image)
      
      rot350 = im.rotate(350)
      rot350.save(str_past_dir+"/"+"z4_rot350_"+image)
      
      rot5 = im.rotate(5)
      rot5.save(str_past_dir+"/"+"z5_rot5_"+image)
      
      rot355 = im.rotate(355)
      rot355.save(str_past_dir+"/"+"z6_rot355_"+image)
      
print("Под 10% перевернуты против часовой")
print("Под 10% перевернуты по часовой")
print("Под 5% перевернуты против часовой")
print("Под 5% перевернуты по часовой")    
