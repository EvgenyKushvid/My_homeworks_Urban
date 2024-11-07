from datetime import datetime
from pprint import pprint
from threading import Thread
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import pandas as pd

cr_base = pd.read_excel('crypto.xlsx', index_col= 0)
names = cr_base['name'].tolist()
names_new = []
for i in names:
        index = names.index(i)
        names_new.append((index,i))

#print(names_new)

cur_price = [] #текущая цена

class Crypto(Thread):
        time_start = datetime.now()
        def __init__(self, cr, index):
                self.cr = cr
                self.index = index
                super().__init__()
                #self. url = 'https://api.coinbase.com/v2/exchange-rates?currency=' + cr[ 0]
                self. url = 'https://api.coinbase.com/v2/exchange-rates?currency=' + cr

        def run (self):
                response  = requests.get(self.url)
                data  =  response.json()
                price  = data['data']['rates']['USDT']
                cur_price.append((self.cr,price))



time_start = datetime.now()



thr_ = []
for cr in names_new:
        try:
                thread = Crypto(cr[1], cr[0])
                thread.start()
                thr_.append(thread)
        except :
                print(f'Нет данных о валюте {cr}')
for th in thr_:
        th.join()

def graf (cur_price):

        data_graf_cr = cr_base['name'].tolist()
        data_graf_total = cr_base['sum_current'].tolist()
        dpi = 80
        fig = plt.figure(dpi = dpi, figsize=(500/dpi,500/dpi))
        mpl.rcParams.update({'font.size': 9})

        plt.title('Распределение активов по криптовалютам')

        xs = range(len(data_graf_cr))

        plt.pie(
            data_graf_total, autopct='%.1f', radius = 1.1,
            explode = [0.15] + [0 for _ in range(len(data_graf_cr) - 1)] )
        plt.legend(
            bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
            loc = 'lower left', labels = data_graf_cr)
        fig.savefig('pie.png')
graf(cur_price) #строим круговую диаграграмму распределения


#  найти индекс валюты... сличеним списков (переделать)
dic = {}
for i in cur_price:
        index = names.index(str(i[0]))
        dic[index] = (str(i[0]),round(float(i[1]),3) )
        #print('---->',i[0],i[1], index+1)
sorted_dict = dict(sorted(dic.items()))
#print('Sorted ', sorted_dict)
#  пищем данные в корент прайс
cr_base.loc[:, "current_price"] = [value[1] for key, value in sorted_dict.items()]
cr_base.to_excel('crypto.xlsx')
# рачситываем таблицу заново

cr_base ['sum_current'] = cr_base['quantity'] * cr_base['current_price']
cr_base ['sum_purchase'] = cr_base['quantity'] * cr_base['purchase']
cr_base ['profit'] = cr_base['sum_current'] - cr_base['sum_purchase']
print(cr_base)

cr_base.to_excel('crypto.xlsx')

sum_profit = round(sum(cr_base['profit'].tolist()),3)
sum_current  = round(sum(cr_base['sum_current'].tolist()),3)



print(f'current profit on {datetime.today()} : {sum_profit} USDT')
print(f'Всего активов на  {sum_current} USDT')

# Печать DataFrame без ограничения максимального числа строк
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(cr_base)

# with pd.ExcelWriter('crypto.xlsx', engine="openpyxl", mode="a") as writer:
#     cr_base.to_excel(writer, index=False, sheet_name='processing')
#cr_base.to_excel('crypto.xlsx')

time_end = datetime.now()


print(f'Время работы потоков {time_end - time_start}')


