import requests
from bs4 import BeautifulSoup

from scrapers.movie_scraper import MovieScraper

BASE_URL = "https://www.imdb.com"


class IMDbScraper(MovieScraper):

    def __init__(self, url: str, quantity: int):
        self.url = url
        self.quantity = quantity
        super().__init__()

    def scrape_movies(self):
        self.logger.info("Starting scraping process...")

        page = requests.get(BASE_URL + self.url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        movie_tags = soup.find_all(
            'td',
            class_='titleColumn'
        )[:self.quantity]
        rating_tags = soup.find_all(
            'td',
            class_='ratingColumn imdbRating'
        )[:self.quantity]

        movies = []

        for movie_tag, rating_tag in zip(movie_tags, rating_tags):
            title = movie_tag.a.text
            rating = float(rating_tag.strong.text)
            summary_url = f"{BASE_URL}{movie_tag.a['href']}"
            summary = self._scrape_summary(summary_url)
            movies.append((title, rating, summary))
            self.logger.info(f"Scraped {title}")

        self.logger.info("Scraping process finished!")

        return movies

    def _scrape_summary(self, url: str):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        summary = soup.find('span', class_='sc-5f699a2-0')
        return summary.text.strip() if summary else "not_summary_found"
