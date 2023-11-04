import os
from PIL import Image
from PIL import ImageFilter

filenameTest = os.listdir("./Diplom/Set_start")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Diplom/Set_start"+"/"+obj)
   str_past_dir = "./Diplom/Set_start/"+obj
   folder = os.makedirs("./Diplom/Set_ready_224/{}".format(obj), exist_ok=True)
   str_new_dir = "./Diplom/Set_ready_224/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((224,224))
      new_im.save(str_new_dir+"/"+image)

filename = os.listdir("./Diplom/Set_ready_224")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Diplom/Set_ready_224"+"/"+obj)
   str_past_dir = "./Diplom/Set_ready_224/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      
      det_d = im.filter(ImageFilter.DETAIL)
      det_d.save(str_past_dir+"/"+"z1_det_"+image)
      
      det_s = im.filter(ImageFilter.SMOOTH)
      det_s.save(str_past_dir+"/"+"z2_smooth_"+image)
      
print("Применен фильтр улучшения деталей, который сделает детали более очевидными для тестовых")  
print("Применен плавный фильтр для тестовых")

for obj in filename:
   past_dir = os.listdir("./Diplom/Set_ready_224"+"/"+obj)
   str_past_dir = "./Diplom/Set_ready_224/"+obj
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
      
print("Под 10% перевернуты против часовой для тестовых")
print("Под 10% перевернуты по часовой для тестовых")
print("Под 5% перевернуты против часовой для тестовых")
print("Под 5% перевернуты по часовой для тестовых") 

for obj in filename:
   past_dir = os.listdir("./Diplom/Set_ready_224"+"/"+obj)
   str_past_dir = "./Diplom/Set_ready_224/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      width,height = im.size
      new_width = int(width * 0.88)  # 12% уменьшения ширины
      new_height = int(height * 0.88)  # 12% уменьшения высоты
      left = (width - new_width) // 2
      top = (height - new_height) // 2
      right = left + new_width
      bottom = top + new_height
      im_cropped = im.crop((left, top, right, bottom))
      im_final = im_cropped.resize((224, 224))
      im_final.save(str_past_dir+"/"+"z7_crop_"+image)

print("Добавлены обрезанные изображения для тестовых")
