#vypíše všecjny pátky 13. v zadaném intervalu

import datetime

first_date = input('Zadejte 1. datum (př. 1.1.2020): ')
second_date = input('Zadejte 2. datum: ')
first_date_boiled = datetime.datetime.strptime(first_date, '%d.%m.%Y')
second_date_boiled = datetime.datetime.strptime(second_date, '%d.%m.%Y')

delta = datetime.timedelta(1)
days = list()
while first_date_boiled != second_date_boiled:
    if (first_date_boiled.day == 13) and (first_date_boiled.weekday() == 4):
        days.append(first_date_boiled.strftime(' %Y-%m-%d'))
    first_date_boiled += delta

print(days)



