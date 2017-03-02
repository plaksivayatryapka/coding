#! /usr/bin/env python
# -*- coding: utf-8 -*-


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def read_csv(csv_input_filename, columns_to_return):
    import csv
    with open(csv_input_filename, 'rt') as input_file:
        data = list(csv.reader(input_file, delimiter='\t'))

    input_file.close()
    return tuple(map(list, zip(*data)))[:columns_to_return]


def write_csv(data, filename):
    import csv
    with open(filename, 'wb') as output_file:
        write = csv.writer(output_file)
        for row in data:
            write.writerow(row)

    output_file.close()


def generate_date_range(date_start, periods_count, period_size):
    import pandas
    if period_size == 'month':
        dates = pandas.date_range(date_start, periods=periods_count, freq='MS')
    elif period_size == 'hour':
        dates = pandas.date_range(date_start, periods=periods_count, freq='60 min')
    elif period_size == 'year':
        dates = pandas.date_range(date_start, periods=periods_count, freq='AS')
    return dates


def draw(dates, data, title, y_axis_name, filename):
    import matplotlib.pyplot as plt
    plt.plot(dates, data)
    plt.set_title(title)
    plt.ylabel(y_axis_name)
    plt.savefig(filename)