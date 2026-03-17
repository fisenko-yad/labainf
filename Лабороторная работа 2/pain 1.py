salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
current_spend = spend
month = 0
while month < months:
    if month > 0:
        current_spend = current_spend * (1 + increase)
    if current_spend > salary:
        money_capital += current_spend - salary
    month += 1
money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
