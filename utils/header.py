import xlrd
import re
import pandas as pd

from os import listdir
from os.path import isfile, join

data_path = '../../data/PlugLoad-Equipment/'
data_files = [files for files in listdir(data_path) if isfile(join(data_path, files))]
# data_files = ['combination_ovens_retrofits.xlsx']
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

    '''List out Header Elements'''
    hdr_row_1 = sheet.row(header_row - 1)
    hdr_row_2 = sheet.row(header_row)

    print [label.value for label in hdr_row_2]

    # break
