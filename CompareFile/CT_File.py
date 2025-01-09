import re


English = r'[ \t]*([0-9A-Za-z_. \-\(\)]*[A-Za-z0-9\(\)]+)[ ]*=[ ]*"(.*)"[, ]*'
Korean = r'[ \t]*([0-9A-Za-z_. \-\(\)]*[A-Za-z0-9\(\)]+)[ ]*=[ ]*".*"[, ]*'

output = []
filename = ''
with open("./CompareFile/0_Origin.txt", "r", encoding = 'utf-8') as origin :
    with open("./CompareFile/1_Trans.txt", "r", encoding = 'utf-8') as trans :
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
            
        print(output)
                    

with open("./CompareFile/Output.txt", mode = "w", encoding = 'utf-8') as items:
    items.write(filename)
    for item in output:
        items.write('\t' + item[0] + ' = "'+ item[1] + '",\n')
    items.write('}')
    