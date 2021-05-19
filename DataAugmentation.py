from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img
import os
import time

datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
                            height_shift_range=0.1,shear_range=0.15,
                            zoom_range=0.1,channel_shift_range = 10,
                            horizontal_flip=True)

path = 'D:/CORPUS/1024-1024/Asian/'
filename = os.listdir('D:/CORPUS/1024-1024/Asian')
save_path = "D:/CORPUS/1024-1024-augmented/asian"
cnt=0
start_time = time.time()
for f in filename:
    cnt+=1
    print("img " + str(cnt) + "/" + str(len(filename)))
    img = load_img(path+f)
    x = img_to_array(img)
    x = x.reshape((1,)+ x.shape)
    i=0
    for batch in datagen.flow(x, batch_size= 1,
                              save_to_dir=save_path,
                              save_prefix=f[:-4],
                              save_format="jpeg"):
        i+=1
        print(str(i)+"/10")
        if i > 10:
            break

print(time.time() - start_time)

