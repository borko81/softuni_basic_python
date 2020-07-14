"""
Великденските празници наближават и местната пекарна започва да набавя продуктите, които ще са ѝ нужни за изработка на великденските сладкиши. Вашата задача е да напишете програма, която да изчислява нужната сума за закупуване на продуктите. Нужните продукти са: брашно, захар, яйца и мая. От конзолата се въвежда цената на брашното за килограм, нужните килограми брашно, килограмите захар, броя на корите с яйца и пакетите мая.
    • цената на килограм захар е с 25% по-ниска от тази на килограм брашно
    • цената на една кора с яйца е с 10% по-висока от цената на килограм брашно
    • цената на един пакет мая е с 80% по-ниска от цената на килограм захар
"""

mehl_price = float(input())
mehl_quantity = float(input())
sugar_quantity = float(input())
eggs = float(input())
maq = float(input())

sugar_price = mehl_price - mehl_price * 0.25
eggs_price = mehl_price + mehl_price * 0.1
maq_price = sugar_price - sugar_price * 0.8

total = mehl_price * mehl_quantity + sugar_quantity * sugar_price + eggs * eggs_price + maq * maq_price

print(f'{total:.2f}')