import sys
import os
import numpy as np

def load_paths(path_to_dir):
    paths=[]
    for folder in os.listdir(path_to_dir):
        in_folder_path=path_to_dir+'/'+folder
        for file in os.listdir(in_folder_path):
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
        
def load_val(image_dir,label_dir):
    dataset = {'validation':[]}
    
    val_image_paths=load_paths(image_dir)
    val_label_paths=load_paths(label_dir)

    load_datasets(dataset['validation'],val_image_paths,val_label_paths)

    return dataset