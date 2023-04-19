import argparse

from scrapers.imdb_scraper import IMDbScraper
from writers.csv_writer import CSVWriter

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_args():
    parser = argparse.ArgumentParser(description='Scrape movies')
    parser.add_argument(
        'relative_url',
        type=str, help='URL to scrape movies from'
    )

    parser.add_argument(
        '--scraper',
        '-s',
        type=str,
        default='imdb',
        help='Scraper to use'
    )

    parser.add_argument(
        '--output',
        '-o',
        type=str,
        default='top_movies.csv',
        help='Output file name'
    )

    parser.add_argument(
        '--quantity',
        '-q',
        type=int,
        default=10,
        help='Quantity of movies to scrape'
    )

    return parser.parse_args()


SCRAPERS = {
    'imdb': IMDbScraper
}

if __name__ == '__main__':
    args = get_args()
    scraper = SCRAPERS[args.scraper](args.relative_url, args.quantity)
    movies = scraper.scrape_movies()
    writer = CSVWriter(args.output)
    writer.write(movies)
