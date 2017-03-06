
#from functions import read_csv


def read_csv(csv_input_filename, columns_to_return):
    import csv
    with open(csv_input_filename, 'rt') as input_file:
        data = list(csv.reader(input_file, delimiter='\t'))

    input_file.close()
    return data


def write_csv(data, filename):
    import csv
    with open(filename, 'wb') as output_file:
        write = csv.writer(output_file)
        for row in data:
            write.writerow(row)

    output_file.close()

wind = read_csv('data/portugal_wind.csv', 1)
new_wind = []
for i in wind:
    #if i != []:
        print i
        new_wind.append(i)
print new_wind
#dolpwrite_csv(new_wind, 'data/portugal_wind_new.csv')