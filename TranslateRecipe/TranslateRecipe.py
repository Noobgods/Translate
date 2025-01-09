import re

output = []
with open("./TranslateRecipe/input.txt", mode = "r", encoding='utf-8') as items:
    while True:
        line = items.readline()

        if not line:
            break
        
        if line == '\n':
            output.append('\n')
            continue

        modename = (re.findall(r'([\t ]*-- [^!]*)', line))
        if modename:
            output.append(modename[0])
            continue

        make = (re.findall(r'([/0-9A-Za-z_=\- \t]*)"Make ([A-Za-z /()-^"]*)"', line))
        if make :
            output.append(make[0][0] + '"' + make[0][1] +' 제작",\n')
            continue

        dismantle = (re.findall(r'([/0-9A-Za-z_=\- \t]*)"Dismantle ([A-Za-z /()-^"]*)"', line))
        if dismantle :
            output.append(dismantle[0][0] + '"' + dismantle[0][1] +' 분해",\n')
            continue

        repair = (re.findall(r'([/0-9A-Za-z_=\- \t]*)"Repair ([A-Za-z /()-^"]*)"', line))
        if repair :
            output.append(repair[0][0] + '"' + repair[0][1] +' 수리",\n')
            continue

        cut = (re.findall(r'([/0-9A-Za-z_=\- \t]*)"Cut ([A-Za-z /()-^"]*)"', line))
        if cut :
            output.append(cut[0][0] + '"' + cut[0][1] +' 자르기",\n')
            continue

        item = (re.findall(r'(ItemName[/0-9A-Za-z_= .\t\-]*"[가-힣A-Za-z /()-^"]*")', line))
        if item :
            output.append('\t' + item[0] + ',\n')
            continue



with open("./TranslateRecipe/output.txt", mode = "w", encoding='utf-8') as items:
    for item in output:
        item = item.replace(' Hood', ' 후드')
        item = item.replace(' Door', ' 문')
        item = item.replace(' Seat', ' 좌석')
        item = item.replace(' Lid', ' 덮개')
        item = item.replace(' Bullbar', ' 불바')
        item = item.replace(' Muffler', ' 머플러')
        item = item.replace(' Sideskirts', ' 사이드스커트')
        item = item.replace(' Tires', ' 타이어')
        item = item.replace(' Tire', ' 타이어')
        item = item.replace(' Armored', ' 장갑')
        item = item.replace(' Armor', ' 장갑')
        item = item.replace(' Bumper', ' 범퍼')
        item = item.replace(' Rear Windshield', ' 후면 유리창')
        item = item.replace(' Windshield', ' 전면 유리창')
        item = item.replace(' Rollbar', ' 롤바')
        item = item.replace(' Front Window', ' 앞 유리')
        item = item.replace(' Rear Window', ' 뒷 유리')
        item = item.replace(' Window', ' 유리창')
        item = item.replace(' Sidesteps', ' 사이드스텝')
        item = item.replace(' Mudflaps', ' 머드플랩')
        item = item.replace(' Roofrack', ' 루프랙')
        item = item.replace(' Reinforced', ' 강화')
        item = item.replace(' Trunk', ' 트렁크')
        item = item.replace(' Front', ' 앞')
        item = item.replace(' Rear', ' 뒤')
        item = item.replace(' Double', ' 이중')
        item = item.replace(' Side', ' 측면')

        if  item.find('--') == -1:
            item = item.replace('Pontiac Firebird ', '폰티악 파이어버드 ')
            item = item.replace('Nissan ', '닛산 ')
            item = item.replace('Camaro ', '카마로 ')
            item = item.replace('Dodge ', '닷지 ')
            item = item.replace('Challenger ', '챌린저 ')
            item = item.replace('Caravan ', '카라반 ')
            item = item.replace('Plymouth Barracuda ', '플리머스 바라쿠다 ')
            item = item.replace('Chevrolet ', '쉐보레 ')
            item = item.replace('Jeep ', '지프 ')
            item = item.replace('Ford ', '포드 ')
            item = item.replace('Econoline ', '이코노라인 ')
            item = item.replace('Volkswagen Golf ', '폭스바겐 골프 ')
            item = item.replace('Pierce Arrow ', '피어스 애로우 ')
            item = item.replace('Range Rover ', '레인지 로버 ')
            item = item.replace('Skyline ', '스카이라인 ')
            item = item.replace('Suburban ', '서버번 ')
            item = item.replace('Mustang ', '머스탱 ')
            item = item.replace('Bronco ', '브롱코 ')
            item = item.replace('Crown Victoria Police Interceptor ', '크라운 빅토리아 경찰 인터셉터 ')

        print(item)
        items.write(item)
    