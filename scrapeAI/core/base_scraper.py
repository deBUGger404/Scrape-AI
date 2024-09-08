import re
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class BaseScraper:
    def __init__(self, llm):
        self.llm = llm

    def analyze_page(self, html_content, user_query, token):
        instruction = (
            "Analyze the provided HTML content to determine if the information relevant to the user's query is directly "
            "available on the page. If the required information is present without any interactions, such as searching or filtering,"
            " simply extract and provide the content, responding with 'DIRECT'. However, if the user explicitly requests to perform a search, "
            "apply a filter, or if the data retrieval requires additional interactions, proceed with performing the search or filtration and "
            "respond with 'SEARCH'. Ensure that you only perform searches or filtering actions when necessary or requested by the user, and "
            "prioritize direct scraping of content whenever it is immediately available."
            "Strictly, Respond with either 'DIRECT' or 'SEARCH'"
        )
        messages = [
            {"role": "system", "content": "You are an expert in web page analysis."},
            {"role": "user", "content": f"User Query: {user_query}\n\nHTML Content:\n{str(html_content)[:token]}...\n\n{instruction}"}
        ]
        response = self.llm.chat_completions_create(messages=messages)
        return response.choices[0].message.content.strip()

    def get_extraction_code(self, html_chunk, user_query, token, previous_code=None, error_message=None):
        instruction = (
            "Provide Python code to extract information related to the user's query from the HTML "
            "chunk. The HTML content will be stored in the 'html_chunk' variable (do not define 'html_chunk' "
            "in the code). The fields to be extracted should depend on the user's query, so make sure the extracted "
            "information is relevant to what the user is asking for. Use BeautifulSoup for parsing. Return the extracted "
            "information as a list of dictionaries named 'extracted_info'. Each dictionary should contain the fields requested "
            "by the user (e.g., title, link, description, or any other relevant fields). Ensure that the code handles cases where "
            "elements may be missing. Use only Selenium and BeautifulSoup libraries, not others(e.g.webdriver-manager, playwright)."
            "Wrap the code in <python></python> tags. Do not include any explanations or sample data."
        )
        if error_message:
            instruction += f"\nThe previous code resulted code: {previous_code} \n and this is error we are getting from the code: {error_message}. Please provide a corrected version."

        messages = [
            {"role": "system", "content": f"You are an expert in web scraping with BeautifulSoup.{instruction}"},
            {"role": "user", "content": f"User Query: {user_query}\n\nhtml_chunk:\n{str(html_chunk)[:token]}"}
        ]

        logging.info(f'extraction prompt:{messages}')
        response = self.llm.chat_completions_create(messages=messages)
        return self.extract_code(response.choices[0].message.content.strip())

    def extract_code(self, content):
        match = re.search(r'<python>(.*?)</python>', content, re.DOTALL)
        return match.group(1).strip() if match else content.strip()

    def extract_info(self, html_content, extraction_code):
        local_vars = {'BeautifulSoup': BeautifulSoup, 'html_chunk': html_content}
        exec(extraction_code, globals(), local_vars)
        return local_vars.get('extracted_info', [])