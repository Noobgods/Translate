import os
import chardet
import re
import time
import deepl

url_for_deepl = 'https://api-free.deepl.com/v2/translate'

auth_key = 'b021e2cb-7c16-48e5-9cb8-2443d3a05408:fx'
translator = deepl.Translator(auth_key)

rkey = r'#. Key:\s([A-Z0-9a-z_]*)\n'
rmsgctxt = r'msgctxt\s?"(.*)"\n'
rmsgid = r'msgid\s?"(.*)"\n'
rmsgstr = r'msgstr\s?"(.*)"'

path_EN = '.\\EN\\'
path_KO = '.\\KO\\'

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
    

readfile = ''
splitfile = []
for file_EN in EN:
    enc_en = detfile(f'{path_EN}/{file_EN}')
    if not enc_en :
        continue
    
    with open(f"{path_EN}/{file_EN}", mode = "r", encoding = 'utf-8') as engf:
        readfile = engf.read()

        splitfile = readfile.split('\n\n')

arrtxt = []
for obj in splitfile[2:]:
    txt = re.findall(rmsgctxt, obj)
    id = re.findall(rmsgid, obj)
    str = re.findall(rmsgstr, obj)

    if not txt : 
        txt = ''
    else : 
        txt = txt[0]

    if not id : 
        continue
    else : 
        id = id[0]

    if not str : 
        continue
    else : 
        str = str[0]

    arrtxt.append({'txt' :txt, 'id' : id, 'str' : str})

for file_KO in EN:
    enc_ko = detfile(f'{path_EN}/{file_KO}')
    if not enc_ko :
        continue
    with open(f"{path_KO}/{file_KO}", mode = "a", encoding = 'utf-8') as korf:
        i = 0
        for sf in splitfile[2:]:
            if not sf : continue
            elif -1 != sf.find('msgstr') and -1 != sf.find('Glimpse.Subtitle'):
                ttxt = translator.translate_text(arrtxt[i]['id'], target_lang="KO").text
                korf.write(re.sub(rmsgstr, 'msgstr "'+ ttxt +'"\n\n', sf))

                print(ttxt)
                time.sleep(0.3)

            else :
                korf.write(sf + '\n\n')
            i += 1