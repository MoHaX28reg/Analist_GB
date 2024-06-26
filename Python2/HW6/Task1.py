#  В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from datetime import datetime as dt
from calendar import isleap
from sys import argv

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True
    except:
        return False


def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")


if __name__=="__main__":
    arg_data = argv[1]
    print(check_date(arg_data))