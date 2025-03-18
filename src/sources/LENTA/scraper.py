from urllib.parse import urljoin
from bs4 import BeautifulSoup

from ..base import SimpleScraper


class LENTA(SimpleScraper):
    def __init__(self, source_id):
        super().__init__(source_id=source_id, url="https://lenta.ru/parts/news/")

    def parse_soup(self, soup: BeautifulSoup):
        news_list = []
        for news in soup.find_all(class_="card-full-news _parts-news"):
            url = urljoin(self.url, news["href"])
            title = news.h3.text.strip()
            news_list.append({"url": url, "title": title})
        return news_list
