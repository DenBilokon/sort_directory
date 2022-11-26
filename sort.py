from pathlib import Path
import re

def normalize_names(name):
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


def sort(path):

    list_image = ['JPEG', 'PNG', 'JPG', 'SVG']
    list_video = ['AVI', 'MP4', 'MOV', 'MKV']
    list_documents = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
    list_music = ['MP3', 'OGG', 'WAV', 'AMR']
    list_archives = ['ZIP', 'GZ', 'TAR']

    for txt_path in Path(path).glob("**\*.*"):
        last_name = normalize_names(txt_path.name)








#print(sort("C:/Users/BohdanBilokon/Desktop/Motlox"))






