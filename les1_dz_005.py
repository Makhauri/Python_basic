#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = input('Введите прибыль вашего предприятия: ')
cost = input('Введите издержки вашего предприятия: ')

if int(profit) < int(cost):
    print('Ваше предприятие убыточно')
else:
    print('Ваше предприятие прибыльно')
    print(f'Соотношение прибыли к убыткам = 1 к {int(profit)/int(cost)}')

    staff = input('Введите число сотрудников: ')
    print(f'Прибыль на каждого сотрудника составляет: {int(profit)//int(staff)} рублей {int(profit)%int(staff)} копеек')