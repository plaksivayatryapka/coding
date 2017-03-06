from functions import read_csv, write_csv
from functions_renew import calculate_cycle

import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

load_saved, wind_saved, solar_saved = read_csv('data/renew.csv', 3)
wind_saved = list(map(float, wind_saved))
solar_saved = list(map(float, solar_saved))
load_saved = list(map(float, load_saved))

filename = 'cycles.png'


wind_multipliers = []
solar_multipliers = []
wind_m_result = []
solar_m_result = []
lcoe_result = []
capacity_storages = []
capacity_storage_result = []
gas_ratio_result = []
overhead_ratio_result = []

lcoe_wind = 65
lcoe_solar = 65
lcoe_gas = 65

wind_price = 2  # leads to LCOE = 65
solar_price = 1  # leads to LCOE = 65
gas_price = 1  # leads to LCOE = 65

price_kwh_storage = 150
discount_rate_storage = 1.045
years_storage = 15

wind_rng = 20
solar_rng = 40
storage_rng = 1

lcoe_target = 200
gas_ratio_target = 0

step = 1
for i in range(wind_rng):
    wind_multipliers.append(step)
    step += 1

step = 1
for i in range(solar_rng):
    solar_multipliers.append(step)
    step += 1

step = 5000
for i in range(storage_rng):
    capacity_storages.append(step)
    step += 1000

for wind_multiplier in wind_multipliers:
    for solar_multiplier in solar_multipliers:
        for capacity_storage in capacity_storages:
            lcoe, overhead_ratio, gas_ratio = \
                calculate_cycle(wind_saved, solar_saved, load_saved, wind_multiplier, solar_multiplier, capacity_storage, wind_price, solar_price, gas_price,
                                price_kwh_storage, discount_rate_storage, years_storage)
            print wind_multiplier, solar_multiplier, lcoe, capacity_storage, gas_ratio

            if lcoe < lcoe_target and gas_ratio <= gas_ratio_target:
                wind_m_result.append(wind_multiplier)
                solar_m_result.append(solar_multiplier)
                lcoe_result.append(lcoe)
                capacity_storage_result.append(capacity_storage)
                gas_ratio_result.append(gas_ratio)
                overhead_ratio_result.append(overhead_ratio)
                print wind_multiplier, solar_multiplier, lcoe, capacity_storage, overhead_ratio


fig = plt.figure(figsize=(16, 9))
plt.scatter(solar_m_result, wind_m_result, s=100, c=lcoe_result, cmap=plt.cm.coolwarm)
plt.xlabel('solar multiplier')
plt.colorbar()
#plt.ylim(ymin=0, ymax=40)
#plt.xlim(xmin=0, xmax=40)

plt.ylabel('wind multiplier')
plt.grid()

data = [wind_m_result, solar_m_result, lcoe_result, capacity_storage_result, gas_ratio_result, overhead_ratio_result]
data = map(list, zip(*data))
write_csv(data, 'b.txt')

#plt.savefig(filename)
#os.system('gwenview %s' % filename)
