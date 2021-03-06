"""
С наближаването на Великденските празници, цех за боядисване на яйца, започва да боядисва различни размери яйца, които след това продава на партиди. В таблицата са показани размерите на яйцата, различните бои и каква е цената за продажба на една партида яйца, зависеща от размерите и цвета боя.
Напишете програма, която изчислява какви ще са приходите на цеха от продажбите, като знаете размера на яйцата и техният цвят. С 35% от крайната цена ще бъдат покрити производствени разходи.
"""

data = {'Large': {'Red': 16, 'Green': 12, 'Yellow': 9}, \
        'Medium': {'Red': 13, 'Green': 9, 'Yellow': 7}, \
       'Small': {'Red': 9, 'Green': 8, 'Yellow': 5}}

size = input()
color = input()
count = float(input())

price = count * data[size][color]
price_without_kosten = price - price * 0.35
print(f'{price_without_kosten:.2f} leva.')
