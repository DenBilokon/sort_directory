import os
from sort import normalize_names
from pathlib import Path
start_path = "C:/Users/BohdanBilokon/Desktop/Motlox"
dir_images = start_path + "/images"
for txt_path in Path(start_path).glob("**/*.*"):
    list_files = txt_path.name.split(".")
    print(normalize_names(txt_path.name))

    os.rename(txt_path, os.path.join(dir_images, normalize_names(txt_path.name)))







# try:
#     shutil.unpack_archive(new_file, os.path.join(f"{root_direct}","archives", f"{archive_dir}"), format=archive_format)
# except (ValueError, shutil.ReadError):
#     shutil.move(new_file, os.path.join(f"{root_direct}","archives"))
# else:
#     try:
#         shutil.move(os.path.join(f"{path}", f"{file}"),
#         os.path.join(f"{root_direct}", 'others'))
#     except shutil.Error:
#         pass