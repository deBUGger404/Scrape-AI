from .base_scraper import BaseScraper
import logging

logger = logging.getLogger(__name__)

class DirectScraper(BaseScraper):
    def scrape(self, html_content, body_element, user_query, token):
        extraction_code = self.get_extraction_code(body_element, user_query, token)
        logger.info(f"Extraction code:\n{extraction_code}")
        return self.extract_info(html_content, extraction_code)