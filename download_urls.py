import requests


def nume_scrape(URL, MIN, MAX, output="urls.txt"):
    """
    Numerical scraping tool to download web urls if they are in numerical order.
     - Takes [URL | string] to access string.
     - Takes [MIN | int] to define minimum range.
     - Takes [MAX | int] to define maximum of range.
    """

    headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; \
        x64) AppleWebKit/123.45 (KHTML, like Gecko) \
        Chrome/69.0.6969.69 Safari/537.36'
    }


    for page in range (MIN,MAX):
        current_url = URL + '/' + str(page)
        thepage = requests.get(current_url, headers=headers, params={'query': 'interview'}, timeout=40)

        # check page exists and is accessible
        if thepage.status_code != requests.codes.ok:
            continue
        
        # write list to file
        with open(output, 'a', encoding='utf-8') as f:
            f.write(f"\n{current_url}")
        
        print(current_url, thepage.status_code)

if __name__ == "__main__":
    nume_scrape("http://www.en.kremlin.ru/events/president/transcripts", 65030, 70409)