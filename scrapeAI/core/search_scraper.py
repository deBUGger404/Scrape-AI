from .base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class SearchScraper(BaseScraper):
    def get_search_code(self, html_content, user_query, token):
        instruction = (
            "Analyze the HTML content and provide Selenium Python code to interact with the page based on the user's query. "
            "If a search box is present, provide code to use it. If not, provide code to navigate to the most relevant section or interact with the page in a way that's most likely to find the required information. "
            "Use 'By' for element location strategies. You can use 'Keys' if needed. "
            "Use only Selenium and BeautifulSoup libraries, not others(e.g.webdriver-manager, playwright)."
            "Wrap the code in <python></python> tags. Do not include any explanations or comments."
        )
        messages = [
            {"role": "system", "content": f"You are an expert in web scraping using Selenium and analyzing HTML structures.{instruction}"},
            {"role": "user", "content": f"User Query: {user_query}\n\nHTML Content:\n{str(html_content)[:token]}"}
        ]
        response = self.llm.chat_completions_create(messages=messages)
        return self.extract_code(response.choices[0].message.content.strip())

    def scrape(self, html_content, user_query, driver, token):
        search_code = self.get_search_code(html_content, user_query, token)
        logger.info(f"Search code:\n{search_code}")
        
        try:
            exec(search_code, {'driver': driver, 'By': By, 'Keys': Keys, 'WebDriverWait': WebDriverWait, 'EC': EC})
            WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, "body")))
            new_html_content = driver.page_source
            
            extraction_code = self.get_extraction_code(new_html_content, user_query, token)
            return self.extract_info(new_html_content, extraction_code)
        except Exception as e:
            logger.error(f"Error during page interaction and extraction: {str(e)}")
            logger.info("Attempting to extract information from the current page...")
            extraction_code = self.get_extraction_code(html_content, user_query, token, search_code, str(e))
            return self.extract_info(html_content, extraction_code)