import os

instance = 'PROD'

if instance == 'LOCAL':

    os.environ["PARSE_API_ROOT"] = "http://localhost:1337/parse"
    APPLICATION_ID = 'NLI214vDqkoFTJSTtIE2xLqMme6Evd0kA1BbJ20S'
    MASTER_KEY = 'lgEhciURXhAjzITTgLUlXAEdiMJyIF4ZBXdwfpUr'

elif instance == 'PROD':

    os.environ["PARSE_API_ROOT"] = 'http://ec2-18-220-200-115.us-east-2.compute.amazonaws.com:80/parse'
    APPLICATION_ID = '47f916f7005d19ddd78a6be6b4bdba3ca49615a0'
    MASTER_KEY = '275302fd8b2b56dca85f127a6123f281b670c787'

from parse_rest.connection import register
from parse_rest.datatypes import Object
from parse_rest.connection import ParseBatcher

register(APPLICATION_ID, '', master_key=MASTER_KEY)

class PlugLoad(Object):
   pass

## 1. Read the CSV file
## 2. Save the Header to a list
## 3. Iterate through each of the data lines
## 4. Create Plugload Object
## 5. Save it to the Parse Server

import xlrd
import re
import hashlib

from os import listdir
from os.path import isfile, join

data_path = '../../data/PlugLoad-Equipment/'
data_files = [files for files in listdir(data_path) if isfile(join(data_path, files))]
# data_files = ['combination_ovens_retrofits.xlsx']

'''Note: Removing this item as it does not comply with Company - Model Index'''
try:
    data_files.remove('televisions_retrofit_2017.xlsx')
except:
    pass

op_hdr_lines = []
hdr_hash_map = dict()

re_hdr_identifier = re.compile('company', re.IGNORECASE)
hdr_column_index = 1
tbl_column_index = 1

'''Loop through each of the PlugLoad Equipment Files'''
for data_file in data_files:
    print data_file
    file_path = join(data_path, data_file)
    xlsx = xlrd.open_workbook(file_path, encoding_override='cp1252')

    sheet = xlsx.sheet_by_index(0)
    total_rows = sheet.nrows
    total_columns = sheet.ncols

    hdr_row_index = None

    '''Identify the Header Start Row Index'''
    for i in range(0, total_rows):
        if re.search(re_hdr_identifier, sheet.cell(i, hdr_column_index).value):
            hdr_row_index = i
            break

    '''Sanitize the Header Row - Create the Hash Map for each of the Header Items'''
    hdr_row = sheet.row(hdr_row_index)
    hdr_row_sanitized = [lines.value.encode('utf-8').replace('\n', ' ') for lines in hdr_row]
    hdr_hash_map.update({data_file: [hashlib.sha1(lines).hexdigest()[:10] for lines in hdr_row_sanitized]})

    '''Create the Data Row'''

    pl_data_collection = []
    for i in range(hdr_row_index + 1, total_rows):
        data_row = (sheet.row_values(i, start_colx=tbl_column_index, end_colx=len(hdr_row_sanitized)))

        ## 1. Initializing the Plugload Object
        pl_data = dict()
        plugload = PlugLoad(
            type=data_file.replace('.xlsx', ''),
            company=str(data_row[0]),
            model=str(data_row[1])
        )
        plugload.data = dict()

        ## 2. Packing up the Plugload Object with Data
        for i, data in enumerate(data_row):
            field_id = hdr_hash_map.get(data_file)[i]
            plugload.data.update({
                field_id: data
            })

        ## 3. Aggregating the Data to do a Batch Save
        pl_data_collection.append(plugload)

    ## 4. Batch Upload - Parse Server
    batcher = ParseBatcher()
    batcher.batch_save(pl_data_collection)

