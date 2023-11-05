from PIL import Image

im = Image.open('1.jpg')
w,h = im.size
new_im=im.resize((224,224))
new_im.save("2.jpg")