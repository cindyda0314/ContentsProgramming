import os.path as osp


# Problem (1)
def get_max(arr):
    if not arr:
        return None
    big = arr[0]
    for num in arr:
        if num > big:
            big = num
    return big
   

def get_min(arr):
    if not arr:
        return None
    small = arr[0]
    for num in arr:
        if num < small:
            small = num
    return small


def get_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total


def get_mean(arr):
    if not arr:
        return None
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    return total / count


def get_median(arr):
    n = len(arr)
    if n == 0:
        return None
    arr_sorted = sorted(arr)
    mid = n // 2
    if n % 2 == 1:
        return arr_sorted[mid]
    else:
        return (arr_sorted[mid - 1] + arr_sorted[mid]) / 2
    

# Problem (2)
def count_files(paths):
    """
    paths: a list that contains directory and file paths.
    """
    n_files = 0
    for p in paths:
        _, ext = osp.splitext(p)
        if ext != "":
            n_files += 1
    return n_files


def filter_fname(fpaths, word):
    """
    fpaths: a list that contains file paths.
    word: a word that is included in file names.
    """
    fpaths_filtered = []
    for f in fpaths:
        name = osp.basename(f)
        if word in name:
            fpaths_filtered.append(f)
    return fpaths_filtered


def filter_ext(fpaths, ext):
    """
    fpaths: a list that contains file paths.
    ext: file extension (e.g., "jpg", "png")
    """
    fpaths_filtered = []
    for path in fpaths:
        _, a_ext = osp.splitext(path)
        if a_ext.lower() == '.' + ext.lower():
            fpaths_filtered.append(path)
    return fpaths_filtered


def change_fname(fpaths, old_word, new_word):
    """
    fpaths: a list that contains file paths.
    old_word: an old word to be replaced by the new word.
    new_word: a new word to replace the old word.
    """
    fpaths_new = []
    for f in fpaths:
        d = osp.dirname(f)        
        filename = osp.basename(f) 
        name, ext = osp.splitext(filename) 

        if old_word in name: 
            name_new = name.replace(old_word, new_word) 
            new_name = name_new + ext  
            new_path = osp.join(d, new_name)  
            fpaths_new.append(new_path)  
        else:
            fpaths_new.append(f)  
    return fpaths_new


def change_dpath(fpaths, dpath):
    """
    fpaths: a list that contains file paths.
    dpath: a new directory path.    
    """
    fpaths_new = []
    for f in fpaths:
        name = osp.basename(f)
        new_path = osp.join(dpath, name)
        fpaths_new.append(new_path)
    return fpaths_new

