#! /usr/bin/env python
# -*- coding: utf-8 -*-

from functions_renew import draw_renew

start_date = 0
end_date = 30

scenarios_count = 3  # сколько сценариев анализировать. Количество параметров в переменных ниже

wind_multiplier = [15, 7.5, 6.5]  # во сколько раз увеличить модельную (равномерную по 4-м странам) генерацию ветра √ермании. ѕервое значение дл€ первого сценари€ и т. д.
solar_multiplier = [15, 7.5, 6.5]  # во сколько раз увеличить реальную генерацию солнца √ермании
capacity_storage = [5001, 1000, 1000]  # Ёмкость аккумуляции в ГВт*ч. 1300 ГВт*ч эквивалентно суточному потреблению.

# LCOE

lcoe_wind = [65, 65, 65]
lcoe_solar = [90, 90, 90]
lcoe_gas = [70, 70, 70]

# переменные вычисления LCOE хранения

price_kwh_storage = [250, 250, 250]  # цена системы хранени€ э/э за к¬т*ч
discount_rate_storage = [1.045, 1.045, 1.045]  # процент по кредиту (4.5%)
years_storage = [15, 15, 15]  # срок кредита

if __name__ == "__main__":

    draw_renew(scenarios_count, wind_multiplier, solar_multiplier, capacity_storage, lcoe_wind, lcoe_solar, lcoe_gas,
               price_kwh_storage, discount_rate_storage,years_storage, start_date, end_date)
