import os
import pandas as pd

path = 'E:/FF-HQ-resized/'
directory = os.listdir(path)
columns = ['img_path','type']

df = pd.DataFrame(columns=columns)
cnt=0
for img in directory:
    cnt+=1
    print('Img n° ' + str(cnt) +'/' +str(len(directory)))
    new_row = {'img_path':path+img,'type':1}
    df = df.append(new_row,ignore_index=True)

print(df.head())
df.to_csv('E:/csv_file/real.csv',index=False)
