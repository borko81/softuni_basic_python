"""
Деси трябва да заведе котката си на ветеринар, но паркингът се заплаща.
Напишете програма, която пресмята колко общо трябва да се плати за престоя на колата на Деси на паркинга.
Паркингът е различен от останалите и има разнообразен ценоразпис. За всеки четен ден и нечетен час,
паркингът таксува 2.50 лева. Във всеки нечетен ден и четен час таксата е 1.25 лева, във всички останали случаи
се заплаща 1 лев. Таксуването става на всеки изминал час от деня.
секи един от изходите трябва да бъде закръглен до втория знак след десетичната запетая.
"""

days = int(input())
hours_per_days = int(input())

total = 0

for d in range(1, days + 1):
    day_sum = 0
    for h in range(1, hours_per_days + 1):
        if d % 2 == 0 and h % 2 == 1:
            day_sum += 2.5
        elif d % 2 == 1 and h % 2 == 0:
            day_sum += 1.25
        else:
            day_sum += 1
    total += day_sum
    print(f'Day: {d} - {day_sum:.2f} leva')


print(f'Total: {total:.2f} leva')