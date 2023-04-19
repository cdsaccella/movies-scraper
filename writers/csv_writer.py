import csv
import logging


class CSVWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.logger = logging.getLogger(__name__)

    def write(self, movies):
        self.logger.info(
            f"Writing {len(movies)} movies to {self.file_path}..."
        )
        with open(
            self.file_path,
            mode='w', newline='',
            encoding='utf-8'
        ) as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Title', 'Rating', 'Summary'])
            for title, rating, summary in movies:
                writer.writerow([title, rating, summary])
        self.logger.info(f"Writing to {self.file_path} finished!")
