import asyncio
import aiohttp

from typing import List
from abc import abstractmethod, ABC
from loguru import logger
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from src.repositories.news import NewsRepository

class Scraper(ABC):
    def __init__(self, source_id):
        self.source_id = source_id
        self.repository = NewsRepository(source_id)
        self.logger = logger

    @abstractmethod
    async def parse(self, *args, **kwargs): ...

class SimpleScraper(Scraper, ABC):
    def __init__(self, source_id, url):
        super().__init__(source_id=source_id)
        self.url = url
        self.headers = {"user-agent": UserAgent().random}
        self.seconds = 20

    @abstractmethod
    def parse_soup(self, soup) -> List[dict]: ...

    async def parse(self):
        self.logger.info(f"Start {self.__class__.__name__}")
        async with aiohttp.ClientSession() as session:
            headers = {"user-agent": UserAgent().random}
            while True:
                async with session.get(url=self.url, headers=headers) as response:
                    if response.ok:
                        soup = BeautifulSoup(await response.text(), "lxml")
                        news_list = self.parse_soup(soup)
                        await self.repository.update_news(news_list)
                        await asyncio.sleep(self.seconds)
                    else:
                        self.logger.error(f"{self.url} | not ok. {response.status}")
                        await asyncio.sleep(60)
