# Kremlin Data Scraper
A scraper tool to download all of God Emporer Putin's interviews on the Kremlin website. This tool probably only works for the Kremlin website and will likely not work for others as it is both an iterative search tool, and it is specialised for the formatting the Kremlin uses. However, if you want to spend an hour downloading the Kremlin's transcripts, this is the tool to use!

# How To Use:
## The actual scripts -
A brief section on what they each do for understanding.
### These may be useful to other researchers
- Download the data as individual `.txt` files with the [get_data_to_txt](https://github.com/CompanyFirmInc/_ruski/blob/main/get_data_to_txt.py) script. This will create a folder where the script is run, which will contain the data in `.txt` files in the format `PAGEID_Title of Transcript.txt`.
- Convert the data from a `.csv` file to a `.db` with the [csv_to_db](https://github.com/CompanyFirmInc/_ruski/blob/main/csv_to_db.py) script. Works with SQLite and MySQL.

### This is automatically run by both scrapers, and works as a module rather than a script
- Clean emojis and weird text from the data with the [clean_data](https://github.com/CompanyFirmInc/_ruski/blob/main/clean_data.py) script.

### Excel doesn't like the formatting this outputs. We are working on a GUI solution since `.csv` files are nicer to use.
- Download the data to a `.csv` format with [this script](https://github.com/CompanyFirmInc/_ruski/blob/main/get_data.py).

## Configuration

### Find the MIN,MAX range for the scraper:
Open the Kremlin website to the first article you'd like to collect. In the URL there is an ID for the page you are on, something like `http://kremlin.ru/events/president/transcripts/#####` where the hashes are the ID. Copy that ID. Open the script and find the line that says `MIN,MAX = #####,#####`. Change the first value to the ID you copied. Then go to http://kremlin.ru/events/president/transcripts/page/1 and copy the ID for the last first transcript there (or navigate to the end of the range you wish and find the ID) and repeat the process filling in the second number. Make sure the numbers are in the order MIN,MAX not the other way around, or the scraper will not run. You can then proceed to run the tool.

### How to Download:
Run the download tool with the command `python3 -m get_data_to_txt`. This may take an hour or two depending on the range you provide the tool so bear that in mind. It isn't our fault, the Kremlin website is slow. Repeatedly starting and stopping the tool will make the Kremlin's website block your connection for approximately an hour. They also have a list of parts of the site you are allowed to scrape, accessible [here](http://kremlin.ru/robot.txt). If you attempt to scrape any of the disallowed sections of their site they will close the connection to your scraper.

# What does this tool do?
This is a webscraping tool to download and store data from the Kremlin's website. This downloads the transcripts of Putin's meetings with heads of state, his presidential addresses, etc. It uses a pairing of Python libraries, namely BeautifulSoup4 and Requests, to iteratively connect and download the transcripts from their webpage, cleans them with the [above mentioned script](https://github.com/CompanyFirmInc/_ruski/blob/main/clean_data.py), and stores them based on the version you run. As researchers, we found it was more convenient to store them as txt files.

# What Else?
[JoshCodesStuff](https://github.com/JoshCodesStuff) is working on a tool to display these documents using the Python library PySimppleGUIQt which will display the text documents to make it easier to view them without a large amount of context switching.
