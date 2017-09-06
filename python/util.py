import os
import SimpleITK as sitk

def get_image_path(data_dir,image_number):
    """
    gets the image directory assuming something like
    data_dir/Source/image_number/image_number/folder/folder/DICOM
    """
    source_dir = data_dir+'/Aorta1/Source'
    seg_dir = data_dir+'/Aorta1/Segmentation'
    im = str(image_number)
    top_folder = '{}/{}'.format(source_dir,im)

    source_dir = find_root(top_folder)

    #now get seg dir
    top_folder = top_folder.replace('Source','Segmentation')
    
    seg_dir = find_root(top_folder)

    return source_dir,seg_dir

def dcmToNumpy(folder):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(folder)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    image_np = sitk.GetArrayFromImage(image)
    return image_np.copy()

def get_image_and_label(data_dir,image_number):
    source_dir,seg_dir = get_image_path(data_dir,image_number)
    image = dcmToNumpy(source_dir)
    label = dcmToNumpy(seg_dir)
    return image,label

def find_root(path):
    p = path
    while(len(os.listdir(p)) == 1):
        p = p + '/' + os.listdir(p)[0]
    return p