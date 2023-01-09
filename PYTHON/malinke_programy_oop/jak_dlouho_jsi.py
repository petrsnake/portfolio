#Vrátí počet dní od tvého narození
import datetime,copy

born_date = input('Zadej svůj věk narození(př.: 1.1.2000): ')
today = datetime.date.today()
delta_day = datetime.timedelta(1)

born_date = datetime.datetime.strptime(born_date,'%d.%m.%Y')
born_date = born_date.date()
count_days = int(0)

born = copy.copy(born_date)

while born_date != today:
    count_days += int(1)
    born_date += delta_day

count_birthday = int(0)
while born.month != today.month and born.day != today.day:
    count_birthday += 1
    born += delta_day

print(count_days, count_birthday)
