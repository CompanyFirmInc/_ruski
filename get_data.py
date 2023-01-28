import csv
import requests
from bs4 import BeautifulSoup
from time import sleep

if __name__ == "__main__":
    # previously downloaded URL into urls
    with open('urls.txt', 'r', encoding='utf-8') as f:
        body = ""
        data = {'title': '',
            'date': '',
            'time': '',
            'body': ''}

        # create the urls 
        urls = f.readlines()

    with open('data.csv', 'a') as df:
                writer = csv.DictWriter(df, fieldnames=data.keys())
                writer.writeheader()
    
    # take all URLS and run on them
    for URL in urls:
        # data santitization
        URL = URL.replace('\n', '')
        sleep(1)
        
        headers = {'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; \
                    x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/69.0.6969.69 Safari/537.36'}
        # was getting weird error so am using try except
        try:
            # using requests library to see if webpage is available
            thepage = requests.get( URL, headers=headers )

            # no point continuing if the page is gone
            if thepage.status_code == 404:
                print(f"{URL} was moved/deleted!")
                continue

            # using bs4 for accessing webpages and downloading content
            soup = BeautifulSoup(thepage.content, "html.parser")

            # get data
            try:
                title = soup.find("h1", class_="entry-title p-name").get_text()
            except AttributeError as aerr:
                title = ''
            try:
                date = soup.find("time", class_="read__published").get_text()
            except AttributeError as aerr:
                date = ''
            try:
                time = soup.find("div", class_="read__time").get_text()
            except AttributeError as aerr:
                time = ''

            data = {
                'title': title,
                'date': date,
                'time': time,
                'body': ''
            }

            print(data['title'], data['date'], data['time'])

            for para in soup.find("div", class_="entry-content").find_all("p"):
                body += para.get_text()
            
            data['body'] = body

            with open('data.csv', 'a') as df:
                writer = csv.DictWriter(df, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)

        # check page still exists since grabbed url
        except requests.exceptions.MissingSchema as e:
            print (e)