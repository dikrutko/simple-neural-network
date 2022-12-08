import os
from PIL import Image

saple = Image.open('./Training/fourth_pillar/4.JPG')
a1 = saple.resize((318,318))
a1.save('./Training/fourth_pillar/4.JPG')
#a1.save('./Winter')
