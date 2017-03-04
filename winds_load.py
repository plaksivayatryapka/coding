#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib
matplotlib.rc('font', family='DejaVu Sans') # шрифт с поддержкой русского языка
matplotlib.use('agg')
import matplotlib.pyplot as plt
from functions import read_csv, generate_date_range
x_size = 12
y_size = 6
filename = 'winds_and_load.png'

x1, x3, x6, x9, load = read_csv('data/winds_and_load.csv', 5)

rng = len(x1)

dates = generate_date_range('01-01-2015', rng, 'hour')

plt.figure(figsize=(x_size, y_size))
plt.plot(dates, x1, label=u'Выровненный "ветер"')
plt.plot(dates, x3, label=u'Выровненный "ветер" x3')
plt.plot(dates, x6, label=u'Выровненный "ветер" x6')
plt.plot(dates, x9, label=u'Выровненный "ветер" x9')
plt.plot(dates, load, color='k', linewidth=2, label=u'Потребление')

plt.title('Wind generation')
plt.ylabel('GW')
plt.xticks(rotation=25)
plt.grid()
plt.legend()
plt.legend(loc='upper left')
plt.savefig(filename)
os.system('gwenview %s' % filename)
