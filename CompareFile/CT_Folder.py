import re
import os
import chardet
import shutil

English = r'[ \t]*([0-9A-Za-z_.\- ]*[A-Za-z0-9]+)[ ]*=[ ]*"([^가-힣"]*)"[, ]*'
Korean = r'[ \t]*([0-9A-Za-z_.\- ]*[A-Za-z0-9]+)[ ]*=[ ]*".*"[, ]*'

path_EN = 'F:\Program Files\Steam\steamapps\common\ProjectZomboid\media\lua\shared\Translate\EN'
path_KO = 'F:\Program Files\Steam\steamapps\common\ProjectZomboid\media\lua\shared\Translate\KO'

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

def changeKoreanFile(origin, filepath_KO, enc_en):
    filename = ''
    output = []
    enc_ko = detfile(filepath_KO)
    if not enc_ko :
        return
        
    with open(f"{filepath_KO}", "r", encoding = enc_ko) as trans :
        oline = origin.read()
        kline = trans.read()

        filename = oline.splitlines(True)[0]
        filename = filename.replace('EN', 'KO')

        originLine = re.findall(English, oline)
        koreanLine = re.findall(Korean, kline)      

        for o in originLine:
            in_korean = False
            for k in koreanLine:
                if o[0] == k:
                    in_korean = True
                    break
            if not in_korean:
                output.append(o)      
            
        with open(f"./CompareFile/EN/{file_KO}", mode = "w", encoding = 'utf-8') as items:
            items.write(filename)
            for item in output:
                items.write('\t' + item[0] + ' = "'+ item[1] + '",\n')
            items.write('}')


for file_EN in EN :
    filepath_EN = f'{path_EN}/{file_EN}'
    enc = detfile(filepath_EN)
    
    if not enc :
        continue

    with open(f"{filepath_EN}", "r", encoding = enc) as origin :
        inkorf = True
        for file_KO in KO :
            filepath_KO = f'{path_KO}/{file_KO}'
            
            file_EN_comp = file_EN.replace('EN', '')
            file_KO_comp = file_KO.replace('KO', '')

            if file_EN.replace('EN', '') == file_KO.replace('KO', ''): # 파일 이름 비교
                changeKoreanFile(origin, filepath_KO, enc)
                inkorf = False
                break

        if inkorf:
            shutil.copyfile(f"{filepath_EN}", f"./CompareFile/EN/{file_EN}") 
