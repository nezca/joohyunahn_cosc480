import os, html_sanitizer

"""This is the module which has 3 functions such as
   'get_data()',
   'get_list() and
   'count_list()'.
"""
# This Python file provides core algorithms such as
# extracting data from the CSV file,
# searching CSV data file in the Data folder
# and counting that data files to record on the main page.
def get_data():
    """Get data frame from original data
    """
    with open('Trekourse_dataset_original.csv', encoding='UTF8') as file:
        csv_data = []
        for line in file.readlines():
            csv_data.append(line.split(','))
        return csv_data

def get_list():
    """Get names of the trekking courses data
       in the Data folder with sanitizing script code
    """
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    liststr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        liststr = liststr + '<li><i style="color:grey;"><a href="index.py?id={name}">{name}</a></i></li>'.format(name=item)
    return liststr

def count_list():
    """Count number of trekking courses csv files
       in the Data folder
    """
    files = os.listdir('data')
    return len(files)
