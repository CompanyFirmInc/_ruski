import re
from time import perf_counter

def _remove_emoji(string):
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

    start = perf_counter()
    if TRACE==1:
        print('cleaning', filename)

    csv_reader = ""
    with open(filename, 'r', encoding='utf8') as csv_file:
        csv_reader = ''.join([i for i in csv_file]).replace("â€™", "'").replace('\n\n', '\n') # turn entire file into 1 line
        _remove_emoji(csv_reader) # remove all emojis

    # Unfortunately have to read and write in two steps to truncate file properly
    with open(filename, 'w', encoding='utf8') as csv_file:
        csv_file.writelines(csv_reader) # write back to csv without destroying data

    finished = perf_counter() - start
    if TRACE==1:
        print(csv_reader)
    
    print(f'Finished cleaning in {finished:.5f} seconds')
