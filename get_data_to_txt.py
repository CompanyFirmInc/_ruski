"""
Runs a scraper that downloads from the Kremlin
"""
import os
import requests
from time import sleep
from bs4 import BeautifulSoup

from clean_data import clean_body

MIN, MAX = 70400, 70410
URL = "http://www.en.kremlin.ru/events/president/transcripts/"


def main():
    """
    Module takes the above url and searches through the defined
    range numerically in order
    """
    print("running")

    # creates directory if it hasn't been made already
    if not os.path.isdir('text_data'):
        os.makedirs('text_data')

    # this needs the order [MIN -> MAX] you utter numpty
    for num in range(MIN,MAX):
        sleep(1) # prevents banning

        headers = {'User-Agent': 'Mozilla/5.0 \
                (Windows NT 6.1; Win64; x64; rv:47.0) \
                ScrapeBot/3.5)',
                'Connection': 'keep-alive',
                'Keep-Alive': 'timeout=5,max-100'}

        # make the request
        res = requests.get(f"{URL}{num}", headers=headers)

        # no point continuing if the page doesn't exist
        if res.status_code != requests.codes.okay:
            print(f"{URL}{num} is invalid.")
            continue

        # using bs4 for accessing webpages and downloading content
        soup = BeautifulSoup(res.content, "html.parser")

        try:
            # define variables with try except as they sometimes don't appear in page
            try:
                title = soup.find("h1", class_="entry-title p-name").get_text()
            except AttributeError:
                title = ''
            try:
                date = soup.find("time", class_="read__published").get_text()
            except AttributeError:
                date = ''
            try:
                time = soup.find("div", class_="read__time").get_text()
            except AttributeError:
                time = ''

            # create data dict for csv later
            content = ''
            data = {
                'url':      URL,
                'title':    title,
                'date':     date,
                'time':     time
            }

            print(data['title'], '-', data['date'], '-', data['time'])

            for para in soup.find("div", class_="entry-content").find_all("p"):
                try:
                    content += para.get_text()
                except AttributeError:
                    content = ''

            data['body'] = clean_body(content)

            with open(f"./text_data/{num}_{title}.txt", 'w+', encoding='utf-8') as txt_file:
                txt_file.writelines(data['title']+'\n')
                txt_file.writelines(data['date']+' ')
                txt_file.writelines(data['time']+'\n')
                txt_file.writelines(data['url']+'\n\n')
                txt_file.write(content)

        except UnicodeEncodeError as err:
            print(err, f"\nAn Error Occurred: at {num}")
            with open("error.txt", 'a', encoding='utf-8') as file:
                file.write(str(num) + '\n')
            continue


if __name__ == "__main__":
    main()
