import re
import sys
import csv
from time import perf_counter

def clean_body(string):
    """
    Cleans passed text strings for nice readable usage.
    - Takes [filename | string] for the working directory.
    - Takes [TRACE | int] to check whether we are in debug mode.
    """
    print('cleaning...')
    
    string = re.sub("[\xa0\n ]", ' ', string) # remove \n and unicode space
    string = re.sub("[<…>]", '', string)
    string = string.replace('.', '. ').replace('  ', ' ')
    
    return string


def clean_csv(filename='.\data.csv', TRACE=0):
    """
    Cleans CSV files for nice readable formats.
    - Takes [filename | string] for the working directory.
    - Takes [TRACE | int] to check whether we are in debug mode.
    """
    print('cleaning', filename)

    # check performance
    start = perf_counter()
    

    with open(filename, encoding='utf-8') as f_in, \
    open ('clean_data.csv', 'w', newline='', encoding='utf-8') as f_out:
        print(f"File opened: {filename}")

        csv_in = csv.reader(f_in)
        csv_out = csv.writer(f_out)

        n = 0
        for row in csv_in:
            if len(row) > 1:
                row[4] = re.sub("[\xa0\n]", ' ', row[4]) # remove \n and unicode char
                row[4] = re.sub("[<…>]", '', row[4])
                row[4] = row[4].replace('.', '. ')
                csv_out.writerow(row)
            
            x = row[4].split('\n')
            if len(x) > 1:
                print("ERROR: length of string off by too far.")
                sys.exit()
            n+=1
    
    # end timer check
    finished = perf_counter() - start
    
    print(f'Finished cleaning {n} rows in {finished:.6f} seconds')


# if __name__ == "__main__":
#     maxInt = sys.maxsize

#     # decrease maxInt value while OverflowError occurs.
#     while True:
#         try:
#             csv.field_size_limit(maxInt)
#             break
#         except OverflowError:
#             maxInt = int(maxInt/10)
    
#     # clean the csv
#     clean_csv(TRACE=1)