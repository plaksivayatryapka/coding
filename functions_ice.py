def read_csv(csv_input_filename, columns_to_return):
    import csv
    with open(csv_input_filename, 'rt') as input_file:
        data = list(csv.reader(input_file, delimiter='\t'))

    input_file.close()
    return tuple(map(list, zip(*data)))[:columns_to_return]


def generate_date_range(date_start, periods_count, period_size):
    import pandas
    if period_size == 'month' :
        dates = pandas.date_range(date_start, periods=periods_count, freq='MS')
    if period_size == 'hour' :
        dates = pandas.date_range(date_start, periods=periods_count, freq='60 min')
    if period_size == 'year' :
        dates = pandas.date_range(date_start, periods=periods_count, freq='AS')
    return dates


def draw(ice_extent, min_years, max_years, min_trendline, max_trendline, dates_month, dates_year, dates_forecast):
    import matplotlib
    matplotlib.rc('font', family='DejaVu Sans')
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    fig = plt.figure()
    chart1 = fig.add_subplot(211)
    chart2 = fig.add_subplot(212)
    chart1.grid()
    chart2.grid()
    chart1.plot(dates_month, ice_extent)
    chart2.plot(dates_year, min_years)
    chart2.plot(dates_year, max_years)
    chart2.plot(dates_forecast, min_trendline)
    chart2.plot(dates_forecast, max_trendline)


    chart1.set_title('Ice extent in north hemisphere')
    chart2.set_title('Yearly mins and maxs')
    chart1.set_ylabel('Mln square km')
    chart2.set_ylabel('Mln square km')
    plt.ylim(ymin=0)
    plt.savefig('chart.png')