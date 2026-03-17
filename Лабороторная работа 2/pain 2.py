money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while True:
    diff = spend - salary
    if money_capital >= diff:
        money_capital -= diff
        months += 1
    else:
        break
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)