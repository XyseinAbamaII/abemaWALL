import pycbrf.toolbox
import os
import datetime

c =0
while c!=2:
    os.system("cls")
    print("cbrf Terminal v0.0.1")
    print("1 - Запрос котировок валют сегодня")
    print("2 - Выход из терминала")
    try:
        c = int(input())
    except ValueError:
        print("Not corrected input")
    if(c > 3):
        print("выберите число 1, 2, 3")
    if (c == 1):
        al = str(datetime.datetime.now())[:10]
        print(al)
        val = input("Input currency name(USD) \n")
        rates = pycbrf.toolbox.ExchangeRates(al)
        result =rates[val].value
        print(result)
        _ = input("Press enter for continied...")

      
