from .direct_scraper import DirectScraper
from .search_scraper import SearchScraper

class ScraperFactory:
    @staticmethod
    def get_scraper(page_analysis, openai_client):
        if page_analysis == 'DIRECT':
            return DirectScraper(openai_client)
        elif page_analysis == 'SEARCH':
            return SearchScraper(openai_client)
        else:
            raise ValueError(f"Unknown scraping strategy: {page_analysis}")