import csv
import json

'''Loads the CSV data - Creates a Dictionary Map'''
def parse_csv(file_path):
    fh = open(file_path, 'rt')
    form_mapper = dict()
    form_mapper['gemini-form'] = []

    try:
        reader = csv.reader(fh)
        for row in reader:
            if not row[1]:
                continue

            if row[0]:
                section = row[0]
                if 'section_block' in locals():
                    form_mapper.get('gemini-form').append(section_block)

                section_block = dict()
                section_block['section'] = section
                section_block['elements'] = []

            element = row[1]
            element_type = row[2]
            element_options = ''
            element_validation = ''

            if element_type == 'PickerInputRow':
                element_options = row[3]

            element_block = dict()
            element_block['param'] = element
            element_block['data-type'] = element_type
            element_block['default-values'] = element_options
            element_block['validation'] = element_validation

            section_block.get('elements').append(element_block)

    finally:
        fh.close()

    return form_mapper


input_file = 'preaudit.csv'
output_file = 'preaudit.json'
data = parse_csv(input_file)

print(data)
print(json.dumps(data))

'''Writing the JSON Output to a file'''
with open(output_file, 'w') as fp:
    json.dump(data, fp)