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
#cz, ie, es, fr, gb, de, dk, average = read_csv('data/europe_winds.csv', 8)
x1, x3, x6, x9, load = read_csv('data/europe_winds.csv', 8)

#rng = len(cz)
rng = len(x1)

dates = generate_date_range('01-01-2015', rng, 'hour')

plt.figure(figsize=(x_size, y_size))
'''plt.plot(dates, cz, label='czech')
plt.plot(dates, ie, label='ireland')
plt.plot(dates, es, label='spain')
plt.plot(dates, fr, label='france')
plt.plot(dates, gb, label='GB')
plt.plot(dates, de, label='germany')
plt.plot(dates, dk, label='denmark')
plt.plot(dates, average, color='k', linewidth=3)'''

plt.plot(dates, x1, label='czech')
plt.plot(dates, x3, label='czech')
plt.plot(dates, x6, label='czech')
plt.plot(dates, x9, label='czech')
plt.plot(dates, load, label='load')

plt.title('Wind generation')
plt.ylabel('GW')
plt.xticks(rotation=25)
plt.grid()
plt.legend()
plt.legend(loc='upper left')
plt.savefig('europe_winds.png')
os.system('gwenview europe_winds.png')