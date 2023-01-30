import re
import sys
import csv
from time import perf_counter

def remove_emoji(string):
    print("Called remove_emoji()")
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def clean_csv(filename='.\data.csv', TRACE=0):
    """
    Cleans CSV files for nice readable formats.
    - Takes [filename | string] for the working directory.
    - Takes [TRACE | int] to check whether we are in debug mode.
    """
    # check performance
    start = perf_counter()
    
    if TRACE==1:
        print('cleaning', filename)

    c_lines = 0
    with open(filename, encoding='utf-8') as f_in, \
    open ('clean_data.csv', 'w', newline='', encoding='utf-8') as f_out:
        print(f"File opened: {filename}")

        c_in = csv.reader(f_in)
        c_out = csv.writer(f_out)

        for row in c_in:
            if len(row) == 5:
                row[4] = row[4].replace('\n', '').replace('Â', ' ').replace('\n\n', '').replace("â€", "'")
                c_out.writerow(row)

    
    # end timer check
    finished = perf_counter() - start
    
    print(f'Finished cleaning in {finished:.5f} seconds')


if __name__ == "__main__":
    maxInt = sys.maxsize
    while True:
        # decrease the maxInt value by factor 10 
        # as long as the OverflowError occurs.
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)
    clean_csv(TRACE=1)