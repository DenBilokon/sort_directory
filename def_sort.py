from pathlib import Path
import os
import re
import shutil


#start_path = "C:/Users/BohdanBilokon/Desktop/trash"


def normalize_names(name):

    # normalize names from cyrillic to latin

    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    translations = ("a", "b", "v", "g", "d", "e", "e", "j", "z",
                    "i", "j", "k", "l", "m", "n", "o", "p", "r",
                    "s", "t", "u", "f", "h", "ts", "ch", "sh",
                    "sch", "", "y", "", "e", "yu", "ya", "je",
                    "i", "ji", "g")

    trans = {}

    for i, j in zip(cyrillic_symbols, translations):
        trans[ord(i)] = j
        trans[ord(i.upper())] = j.upper()
        name_list = name.split(".")
        name_list[0] = name_list[0].translate(trans)
        name_list[0] = re.sub("\W+", "_", name_list[0])
        name = f"{name_list[0]}.{name_list[1]}"
    return name


def sort_create_files(start_path):

    # create dir

    dir_images = start_path + "/images"
    dir_videos = start_path + "/videos"
    dir_music = start_path + "/music"
    dir_documents = start_path + "/documents"
    dir_archives = start_path + "/archives"
    dir_others = start_path + "/others"

    list_of_dirs = [dir_images, dir_videos, dir_documents, dir_music, dir_archives, dir_others]
    name_of_dirs = ["images", "videos", "music", "documents", "archives", "others"]

    for direct in list_of_dirs:
        try:
            os.mkdir(direct)
        except FileExistsError:
            pass

    # remove and rename files

    list_image = ('JPEG', 'PNG', 'JPG', 'SVG', 'BMP')
    list_video = ('AVI', 'MP4', 'MOV', 'MKV')
    list_documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'RTF', 'XLS')
    list_music = ('MP3', 'OGG', 'WAV', 'AMR')
    list_archives = ('ZIP', 'GZ', 'TAR', 'RAR', '7Z')

    for root, subFolders, files in os.walk(start_path):
        for file in files:
            try:
                txt_path = root + "/" + file
                list_files = file.split(".")

                if list_files[-1].upper() in list_image:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_images)

                elif list_files[-1].upper() in list_video:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_videos)

                elif list_files[-1].upper() in list_music:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_music)

                elif list_files[-1].upper() in list_documents:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_documents)

                elif list_files[-1].upper() in list_archives:
                    filename = normalize_names(file)
                    new_name = os.path.join(root, filename)
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_archives)
                    txt_path = os.path.join(dir_archives, filename)
                    try:
                        shutil.unpack_archive(txt_path, dir_archives)
                    except (ValueError, shutil.ReadError):
                        shutil.move(txt_path, dir_archives)
                    else:
                        try:
                            shutil.move(os.path.join(f"{root}", f"{file}"),dir_archives)
                        except shutil.Error:
                            pass

                else:
                    os.path.join(dir_others, file)
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_others)

            finally:
                continue


# delete folders after removing

    for direct in Path(start_path).glob("*"):
        if direct.is_dir() and direct.name not in name_of_dirs:
            try:
                shutil.rmtree(direct, ignore_errors=True)
            except PermissionError:
                print("Permission error for delete", direct)
                pass
