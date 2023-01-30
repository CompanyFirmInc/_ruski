import csv
import requests as req
from bs4 import BeautifulSoup
from time import sleep
from clean_data import remove_emoji

def main(MIN, MAX, URL = "http://www.en.kremlin.ru/events/president/transcripts/"):
    """
    Numerical scraping tool to download web urls if they are in numerical order.
     - Takes [MIN | int] to define minimum range.
     - Takes [MAX | int] to define maximum of range.
     - Takes [URL | string] to access string.
    """
    body = ""

    # take all URLS and run on them
    for num in range(MIN, MAX):
        sleep(1)  # if we dont sleep then the kremlin bans us which sucks

        URL = URL + str(num)  # define the url to scrape

        # define the headers for the application to communicate with
        headers = {'User-Agent': 'Mozilla/5.0 \
                (Windows NT 6.1; Win64; x64; rv:47.0) \
                ScrapeBot/3.5)'}

        # make the request
        res = req.get(URL, headers=headers)

        # no point continuing if the page doesn't exist
        if res.status_code != req.codes.ok:
            print(f"{URL} is invalid.")
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
            data = {
                'url':      remove_emoji(URL),
                'title':    remove_emoji(title),
                'date':     remove_emoji(date),
                'time':     remove_emoji(time),
                'body':     body
            }

            print(data['title'], '-', data['date'], data['time'])

            for para in soup.find("div", class_="entry-content").find_all("p"):
                try:
                    body += para.get_text()
                except:
                    body = ''

            data['body'] = remove_emoji(body)

            with open('data.csv', 'a', encoding='utf-8') as df:
                writer = csv.DictWriter(df, fieldnames=data.keys())
                writer.writerow(data)

        except UnicodeEncodeError as err:
            print(err, f"\nAn Error Occurred: at {num}")
            with open("error.txt", 'a', encoding='utf-8') as f:
                f.write(str(num) + '\n')
            continue


if __name__ == "__main__":
    main(67823, 70409)
