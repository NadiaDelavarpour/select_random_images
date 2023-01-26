#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os
import random
import shutil

img_dir=[]

# specify the existing directory where you want to create the new folder
rootdir = 'F:/Ortho_Data/Barely/CREC_Barley_P4P_150ft_06242021_transparent_mosaic_group1'
listdir = os.listdir(rootdir)
#print(listdir)
for item in listdir:
    if item.endswith('.jpg'):
        path = os.path.join(rootdir, item)
        img_dir.append(path)
        


selected_images_dir = 'selected_images'
# dataset is a list of image file paths
selected_images = random.sample(img_dir, 100)

# create a new folder called 'new_folder' in the existing directory
new_folder = 'selected_images'
new_folder_path = os.path.join(rootdir, new_folder)
os.makedirs(new_folder_path, exist_ok=True)

# get the directory of the new folder
folder_dir = os.path.abspath(new_folder_path)
#print(folder_dir)
for image in selected_images:
    shutil.copy(image, folder_dir)


# In[ ]:




