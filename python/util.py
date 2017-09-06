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
    top_folder = '{}/{}/{}'.format(source_dir,im,im)

    f1 = os.listdir(top_folder)[0]
    f2 = os.listdir('{}/{}'.format(top_folder,f1))[0]

    source_dir = '{}/{}/{}'.format(top_folder,f1,f2)

    #now get seg dir
    top_folder = top_folder.replace('Source','Segmentation')
    f1 = os.listdir(top_folder)[0]
    f2 = os.listdir('{}/{}'.format(top_folder,f1))[0]
    seg_dir = '{}/{}/{}'.format(top_folder.replace('Source','Segmentation'),
        f1,f2)

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
