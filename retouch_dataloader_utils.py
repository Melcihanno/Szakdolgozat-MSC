import sys
import os
import numpy as np
from cross_val_utils import get_train_and_val_folders

def load_paths(path_to_dir,selected_numbers):
    paths=[]
    for folder in os.listdir(path_to_dir):
        in_folder_path=path_to_dir+'/'+folder
        for file in os.listdir(in_folder_path):
            if int(file[:3]) in selected_numbers:
                file_path=in_folder_path+'/'+file
                paths.append(file_path)
    paths.sort()
    return paths

def load_datasets(my_dataset,image_paths,label_paths):
    
    for idx, image_path in enumerate(image_paths):
        label_path = label_paths[idx]
        label=np.load(label_path)
        classes_on_image = (np.unique(label)).tolist()
        dataset_entry = {
            'classes_on_image': classes_on_image,
            'id': idx,
            'image_path': image_path,
            'label_path': label_path
        }
        
        my_dataset.append(dataset_entry)

def load_train_and_val(image_dir,label_dir,fold,iteration):
    dataset = {'train': [],'validation':[]}
    image_paths=[]

    train_numbers,val_numbers = get_train_and_val_folders(fold,iteration)
    
    train_image_paths=load_paths(image_dir,train_numbers)
    train_label_paths=load_paths(label_dir,train_numbers)

    val_image_paths=load_paths(image_dir,val_numbers)
    val_label_paths=load_paths(label_dir,val_numbers)

    load_datasets(dataset['train'],train_image_paths,train_label_paths)
    load_datasets(dataset['validation'],val_image_paths,val_label_paths)

    return dataset