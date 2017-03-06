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
es, fr, gb, de, gr, pt, average = read_csv('data/europe_winds.csv', 7)

rng = len(es)

dates = generate_date_range('01-01-2015', rng, 'hour')

plt.figure(figsize=(x_size, y_size))
#plt.plot(dates, cz, label='czech')
#plt.plot(dates, ie, label='ireland')
plt.plot(dates, es, label='spain')
plt.plot(dates, fr, label='france')
plt.plot(dates, gb, label='GB')
plt.plot(dates, de, label='germany')
#plt.plot(dates, dk, label='denmark')
plt.plot(dates, gr, label='greece')
plt.plot(dates, pt, label='portugal')
plt.plot(dates, average, color='k', linewidth=3, label='average')

plt.title('Wind generation')
plt.ylabel('GW')
plt.xticks(rotation=25)
plt.grid()
plt.legend()
plt.legend(loc='upper left')
plt.savefig('europe_winds.png')
os.system('gwenview europe_winds.png')