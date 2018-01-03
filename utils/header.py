import xlrd
import re
import csv

from os import listdir
from os.path import isfile, join

data_path = '../../data/PlugLoad-Equipment/'
data_files = [files for files in listdir(data_path) if isfile(join(data_path, files))]
output_file = './header_output.csv'
output_lines = []

re_header_identifier = re.compile('company', re.IGNORECASE)
header_start_column = 1

for data_file in data_files:
    print data_file
    file_path = join(data_path, data_file)
    xlsx = xlrd.open_workbook(file_path, encoding_override='cp1252')

    sheet = xlsx.sheet_by_index(0)
    total_rows = sheet.nrows
    total_columns = sheet.ncols

    header_row = None

    '''Header Start Index'''
    for i in range(0, total_rows):
        if re.search(re_header_identifier, sheet.cell(i, header_start_column).value):
            header_row = i
            break

    '''List out Header Elements'''
    hdr_row_1 = sheet.row(header_row - 1)
    hdr_row_2 = sheet.row(header_row)

    hdr_lines = [data_file]
    hdr_lines.extend([lines.value.encode('utf-8').replace('\n', ' ') for lines in hdr_row_2])
    output_lines.append(hdr_lines)


'''Write the Header Output to a File'''
with open(output_file, 'w') as file_obj:
    writer = csv.writer(file_obj, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for line in output_lines:
        writer.writerow(line)
