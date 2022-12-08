import os
from PIL import Image
from PIL import ImageFilter

filenameTest = os.listdir("./Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Test"+"/"+obj)
   str_past_dir = "./Test/"+obj
   folder = os.makedirs("./Set_3/Test/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_3/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filename = os.listdir("./Set_3/Test")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Set_3/Test"+"/"+obj)
   str_past_dir = "./Set_3/Test/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      
      det = im.filter(ImageFilter.DETAIL)
      det.save(str_past_dir+"/"+"z1_det_"+image)
      
      det = im.filter(ImageFilter.SMOOTH)
      det.save(str_past_dir+"/"+"z2_smooth_"+image)
      
print("Применен фильтр улучшения деталей, который сделает детали более очевидными для тестовых")  
print("Применен плавный фильтр для тестовых")

for obj in filename:
   past_dir = os.listdir("./Set_3/Test"+"/"+obj)
   str_past_dir = "./Set_3/Test/"+obj
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

filenameTraining = os.listdir("./Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filenameTest:
   past_dir = os.listdir("./Training"+"/"+obj)
   str_past_dir = "./Training/"+obj
   folder = os.makedirs("./Set_3/Training/{}".format(obj), exist_ok=True)
   str_new_dir = "./Set_3/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      new_im=im.resize((256,256))
      new_im.save(str_new_dir+"/"+image)

filename = os.listdir("./Set_3/Training")   ##Путь к папке для размещения оригинальных изображений

for obj in filename:
   past_dir = os.listdir("./Set_3/Training"+"/"+obj)
   str_past_dir = "./Set_3/Training/"+obj
   for image in past_dir:
      im = Image.open(str_past_dir+'/'+image)
      w,h = im.size
      
      det = im.filter(ImageFilter.DETAIL)
      det.save(str_past_dir+"/"+"z1_det_"+image)
      
      det = im.filter(ImageFilter.SMOOTH)
      det.save(str_past_dir+"/"+"z2_smooth_"+image)
      
print("Применен фильтр улучшения деталей, который сделает детали более очевидными для набора")  
print("Применен плавный фильтр для набора")

for obj in filename:
   past_dir = os.listdir("./Set_3/Training"+"/"+obj)
   str_past_dir = "./Set_3/Training/"+obj
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
      
print("Под 10% перевернуты против часовой для набора")
print("Под 10% перевернуты по часовой для набора")
print("Под 5% перевернуты против часовой для набора")
print("Под 5% перевернуты по часовой для набора")  