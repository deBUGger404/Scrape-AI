from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .core.base_scraper import BaseScraper
from .core.scraper_factory import ScraperFactory
from .utils.html_utils import get_body_ele_without_sidebar
from .llms.llm_factory import LLMFactory
import logging

# Basic configuration for logging
logging.basicConfig(
    # level=logging.DEBUG,  # Set this to DEBUG to capture all levels of logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Custom format
)
logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self, config):
        self.config = config
        self.llm = LLMFactory.create_llm(config['llm'])
        self.token = 30000
        self.verbose = config.get('verbose', False)
        self.headless = config.get('headless', True)
        self.url = config['url']
        self.user_query = config['prompt']

         # Adjust logging level based on verbose setting
        if self.verbose:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

    def invoke(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.get(self.url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            initial_html_content = driver.page_source
            logger.debug("Successfully retrieved page source")
            
            base_scraper = BaseScraper(self.llm)

            body_element = get_body_ele_without_sidebar(initial_html_content)
            page_analysis = base_scraper.analyze_page(body_element, self.user_query, self.token)
            logger.info(f"Page analysis result: {page_analysis}")
            
            scraper = ScraperFactory.get_scraper(page_analysis, self.llm)
            
            if page_analysis == 'DIRECT':
                return scraper.scrape(initial_html_content, body_element, self.user_query, self.token)
            elif page_analysis == 'SEARCH':
                return scraper.scrape(initial_html_content, self.user_query, driver, self.token)
            
        except Exception as e:
            logger.error(f"Error during scraping: {str(e)}")
            return None
        finally:
            driver.quit()
            logger.info("Web driver has been closed")