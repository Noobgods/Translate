import re

match1 = []
match2 = []
lines = []
module = []
with open("./ExtractItems/input.txt", mode = "r", encoding = 'utf-8') as items:
    while True:
        line = items.read()

        if not line:
            break

        module = re.findall(r'module[ \t]*([0-9a-zA-Z\-\(\)]*)[ \t{]*\n', line)
        match1 = re.findall(r'DisplayName[ \t]*=[ \t]*([0-9a-zA-Z /()\-:.]*),[ \t]*\n', line)
        match2 = re.findall(r'item[ \t]*([0-9a-zA-Z\-\(\)]*)[ \t{]*\n', line)

        lines = zip(match2, match1)

        print(match2 , match1)
        print(module)


with open("./ExtractItems/output.txt", mode = "w", encoding = 'utf-8') as items:
    for item in lines:
        items.write('ItemName_' + module[0] + '.' + item[0] + ' = "'+ item[1] + '",\n')
    