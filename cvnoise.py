from skimage import io,util,img_as_ubyte
import os
import numpy as np


def noisy_img_func(img,idx):
    mode = ['gaussian','localvar','poisson','salt','pepper','s&p','speckle']
    return util.random_noise(img,mode=mode[idx])


path = 'D:/CORPUS/1024-1024/Colored/'
filename = os.listdir('D:/CORPUS/1024-1024/Colored')
save_path = "D:/CORPUS/1024-1024-augmented/Colored_noisy/"

cnt=0
for f in filename:
    cnt+=1
    print("img " + str(cnt) + "/" + str(len(filename)+1))
    img = io.imread(path+f)/255.0
    for i in range(7):
        noisy_img = noisy_img_func(img,i)
        io.imsave(save_path+f[:-4]+str(i)+'.jpg',img_as_ubyte(noisy_img))

