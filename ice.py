import numpy
from functions import read_csv, generate_date_range, draw

ice_extent = read_csv('icedata.csv', 1)
ice_extent = list(map(float, ice_extent[0]))
historic_range = len(ice_extent)
min_years = []
max_years = []
year_data = []
month = 0

for ice in ice_extent:
    if 0 <= month <= 11:
        year_data.append(ice)
        month += 1
        if month == 12:
            month = 0
            min_years.append(min(year_data))
            max_years.append(max(year_data))
            year_data = list()

yearly_range = len(min_years)
dates_month = generate_date_range('01-01-1979', historic_range, 'month')
dates_year = generate_date_range('01-01-1979', yearly_range, 'year')
dates_forecast = generate_date_range('01-01-1979', 60, 'year')
all_length = len(dates_forecast)

x = []
for i in range(yearly_range):
    x.append(i)

x_forecast = []
for i in range(all_length):
    x_forecast.append(i)

min_trend = numpy.polyfit(x, min_years, 2)
max_trend = numpy.polyfit(x, max_years, 2)
min_trendline = []
max_trendline = []

x0_min_years = min_years[0]
x0_max_years = max_years[0]
for i in range(yearly_range):
    min_years[i] = min_years[i] / x0_min_years
    max_years[i] = max_years[i] / x0_max_years


x0_min_trend = x_forecast[0] * x_forecast[0] * min_trend[0]+x_forecast[0]*min_trend[1]+min_trend[2]
x0_max_trend = x_forecast[0] * x_forecast[0] * max_trend[0]+x_forecast[0]*max_trend[1]+max_trend[2]

for i in range(all_length):
    min_trendline.append((x_forecast[i] * x_forecast[i] * min_trend[0]+x_forecast[i]*min_trend[1]+min_trend[2])/x0_min_trend)
    max_trendline.append((x_forecast[i] * x_forecast[i] * max_trend[0]+x_forecast[i]*max_trend[1]+max_trend[2])/x0_max_trend)

print min_trendline
draw(ice_extent, min_years, max_years, min_trendline, max_trendline, dates_month, dates_year, dates_forecast)
