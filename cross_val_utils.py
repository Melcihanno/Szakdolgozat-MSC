from collections import defaultdict
import os

CIRRUS=[1,24]
SPECTRALIS=[25,48]
TOPCON=[49,70]

def split_into_folds(arr: list, n: int, i: int):
    
    numbers=list(range(arr[0],arr[1]+1))
    
    folds = defaultdict(list)
    
    for idx, num in enumerate(numbers):
        fold_idx = idx % n  # Körkörösen osztjuk szét
        folds[fold_idx].append(num)
        
    folds=dict(folds)
    
    for fold_idx, nums in folds.items():
        if fold_idx == i:
            train_numbers = [num for num in numbers if num not in nums]
            val_numbers = nums
            
            return train_numbers, val_numbers

def get_train_and_val_folders(folds,iteration):
    all_train = []
    all_val = []
    
    cirrus_train,cirrus_val = split_into_folds(CIRRUS,folds,iteration)
    spectralis_train,spectralis_val = split_into_folds(SPECTRALIS,folds,iteration)
    topcon_train,topcon_val = split_into_folds(TOPCON,folds,iteration)
    
    all_train.extend(cirrus_train)
    all_train.extend(spectralis_train)
    all_train.extend(topcon_train)
    all_val.extend(cirrus_val)
    all_val.extend(spectralis_val)
    all_val.extend(topcon_val)
    
    return all_train, all_val