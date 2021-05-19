from PIL import Image
import os, sys
from tqdm import tqdm

path = 'E:/CORPUS/256-256/female/asian/'
dirs = os.listdir(path)
final_path = 'E:/CORPUS/128-128/female/asian/'
final_size = 128
cnt=0
for item in tqdm(dirs):
 # cnt+=1
  if item == '.DS_Store':
      continue
  if os.path.isfile(path+item):
      #print("Image : " + str(cnt) + " / " + str(len(dirs)))
      im = Image.open(path+item)
      f, e = os.path.splitext(path+item)
      size = im.size
      ratio = float(final_size) / max(size)
      new_image_size = tuple([int(x*ratio) for x in size])
      im = im.resize(new_image_size, Image.ANTIALIAS)
      new_im = Image.new("RGB", (final_size, final_size))
      new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
      new_im.save(final_path+item[:-4]+'.jpg', 'JPEG', quality=90)
