# Phone Information Scraper

It is a simple python tkinter based application to scrape information related to the entered phone number from [find and trace](https://www.findandtrace.com/trace-mobile-number-location) website. The application requires an active internet connection for fetching result

## Requirements

Mechanize : Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mechanize.
Beautifulsoup4 : Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Beautifulsoup4.

```bash
pip install Mechanize
pip install Beautifulsoup4
```

Mechanize is used to parse data to the search bar and press submit button in the find and trace website, beautifulsoup4 will be used to scrape data from the fetched result.

## Usage

Double click the phone_info.pyw to open the GUI application, then enter the phone number in the search box and click the search menu to fetch the related information


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.