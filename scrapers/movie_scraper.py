from abc import ABC, abstractmethod
import logging


class MovieScraper(ABC):

    def __init__(self):
        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def scrape_movies(self):
        pass
