# Web Scraping the Top 10 Movies on IMDB

This Python project is an example of web scraping the top movies on IMDB. The script uses the `beautifulsoup4` library to extract data from the `https://www.imdb.com/chart/top` webpage and save it in a CSV file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries. You need to install the libraries. You can install these libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, simply execute the following command in your terminal:

```python
python main.py /chart/top --scraper imdb --output top_movies.csv --quantity 10
```

The script will create a `top_movies.csv` (`output`) file in the root directory of the repository with the data of the top (`/chart/top`) 10 (`quantity`) movies on IMDB (`scraper`).

Also, you can use the following parameters:
