import re

match = []

with open("./ExtractRecipes/input.txt", mode = "r", encoding = 'utf-8') as items:
    while True:
        line = items.read()

        if not line:
            break

        match = re.findall(r'recipe[ \t]*([0-9a-zA-Z /()-]*)[ \t]*\n', line)
        underline = str.maketrans(' ', '_')

        print(match)

with open("./ExtractRecipes/output.txt", mode = "w", encoding = 'utf-8') as items:
    for item in match:
        items.write('Recipe_' + item.translate(underline) + ' = "' + item + '",\n')
    