import os
import chardet
import re
import time
import deepl

url_for_deepl = 'https://api-free.deepl.com/v2/translate'

auth_key = '9d1a88a1-57a1-4f54-a7f8-f90d334a7aa0:fx'
translator = deepl.Translator(auth_key)

object = r'[\t ]?([0-9A-Za-z. _=/\-\t]*)"(.*)"'

path_EN = './CompareTransFile/EN/'
path_KO = './CompareTransFile/KO/'

EN = os.listdir(path_EN)
KO = os.listdir(path_KO)

def detfile(path):
    if os.path.isfile(path) :
        rawdata = open(f"{path}", "rb").read()
        result = chardet.detect(rawdata)
        enc = result['encoding']

        return enc
    else :
        return False
    
for file_EN in EN:
    enc_en = detfile(f'{path_EN}/{file_EN}')
    if not enc_en :
        continue
    
    with open(f"{path_EN}/{file_EN}", mode = "r", encoding = 'utf-8') as engf:
        readfile = engf.read()       
        objects = re.findall(object, readfile)

        with open(f"{path_KO}/{file_EN}", mode = "a", encoding = 'utf-8') as korf:
            for line in objects:
                if '' != line[1] :
                    text = translator.translate_text(line[1], target_lang="KO").text
                    text = f'\t{line[0]}"{text}",\n'

                    korf.write(text)
                    print(text)
                    
                    time.sleep(0.3)
