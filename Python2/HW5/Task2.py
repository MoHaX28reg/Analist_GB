# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def generator_total_bonus(names_list, rate_list, bonus_list):
    return {name: rate * (1 + float(bonus.strip('%')) / 100) for name, rate, bonus in zip(names_list, rate_list, bonus_list)}


names = ["Василий Иванович", "Петька", "Анка"]
rate = [150000, 123000, 118000]
bonus = ["10.25%", "10.25%", "10.25%"]

print(generator_total_bonus(names, rate, bonus))