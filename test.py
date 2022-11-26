from pathlib import Path
from sort import normalize_names
import os
import shutil

start_path = "C:/Users/BohdanBilokon/Desktop/trash"
list_image = ['JPEG', 'PNG', 'JPG', 'SVG', 'BMP']
list_video = ['AVI', 'MP4', 'MOV', 'MKV']
list_documents = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'RTF', 'XLS']
list_music = ['MP3', 'OGG', 'WAV', 'AMR']
list_archives = ['ZIP', 'GZ', 'TAR' 'RAR', '7Z']

dir_images = start_path + "/images"
dir_videos = start_path + "/videos"
dir_music = start_path + "/music"
dir_documents = start_path + "/documents"
dir_archives = start_path + "/archives"
dir_others = start_path + "/others"

list_of_dir = [dir_images, dir_videos, dir_documents, dir_music, dir_archives, dir_others]
#create dir
for dir in list_of_dir:
    os.mkdir(dir)

#remove dirs
for txt_path in Path(start_path).glob("**/*.*"):
    list_files = txt_path.name.split(".")




    try:
        if list_files[-1].upper() in list_image:
            shutil.move(txt_path, dir_images)
            os.rename(txt_path, os.path.join(dir_images, normalize_names(txt_path.name)))

        if list_files[-1].upper() in list_video:
            shutil.move(txt_path, dir_videos)

        if list_files[-1].upper() in list_music:
            shutil.move(txt_path, dir_music)

        if list_files[-1].upper() in list_documents:
            shutil.move(txt_path, dir_documents)

        if list_files[-1].upper() in list_archives:
            shutil.move(txt_path, dir_archives)

        else:
            shutil.move(txt_path, dir_others)

        try:
            os.rename(txt_path, normalize_names(txt_path.name))

        except FileExistsError:
            os.rename(txt_path, normalize_names(txt_path.name)+"_copy")


    finally:
        continue







