# Scrape-AI

`Scrape-AI` is a Python library designed to intelligently scrape data from websites using a combination of LLMs (Large Language Models) and Selenium for dynamic web interactions. It allows you to configure the library to use a specific LLM (such as OpenAI, Anthropic, Azure OpenAI, etc.) and fetch data based on a user query from websites in real-time. The core functionality enables the agent-like scraping capabilities by leveraging natural language queries.

## Key Features

- **LLM Integration**: Supports multiple LLM models (OpenAI, Anthropic, Azure, Google, etc.) through a flexible factory pattern.
- **Dynamic Web Scraping**: Utilizes Selenium WebDriver to interact with dynamic content on websites.
- **Agent-Like Functionality**: Acts as an intelligent agent that can process user queries and fetch relevant data from the web.
- **Configurable**: Customizable LLM model settings, verbosity, headless browsing, and target URLs.
- **Modular Design**: Structured in a modular way to extend scraping strategies and LLM integrations.

## Installation

1. Clone the repository or install via pip (if available in PyPi):

```bash
pip install scrapeAI
```

2. **Selenium WebDriver Dependencies**:
   Selenium requires a browser driver to interact with the chosen browser. For example, if you're using Chrome, you need to install **ChromeDriver**. Make sure the driver is placed in your system's PATH (`/usr/bin` or `/usr/local/bin`). If this step is skipped, you'll encounter the following error:

```bash
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
```

Here are links to some of the popular browser drivers:

- **Chrome**: [Download ChromeDriver](https://chromedriver.chromium.org/downloads)
- **Edge**: [Download EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **Firefox**: [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Safari**: [WebDriver support in Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

3. Set up your preferred LLM API keys: Ensure you have API keys ready for the LLM model you intend to use (e.g., OpenAI, Azure, Google, Anthropic).

## Usage

Here is a basic usage example of how to use `scrapeAI` to scrape data from a website based on a user query:

```python
from scrapeAI import WebScraper

config = {
    "llm": {
        "api_key": '<Azure OpenAI API KEY>',
        "model": "<Azure OpenAI Deplyement Name>",
        "api_version": "<Azure Open AI API Version>",
        "endpoint": '<Azure OpenAI Endpoint Name>'
    },
    "verbose": False,
    "headless": False,
    "url" : "https://pypi.org/search/?q=genai",
    "prompt" : "Provide all the libraries and their installation commands"
}

scraper = WebScraper(config)

# Invoke the scraping process
result = scraper.invoke()

# Output the result
print(result)
```
The output will be a json as the following:
```markdown
[
  {
    'library': 'genai',
    'installation_command': 'pip install genai'
  },
  {
    'library': 'bookworm_genai',
    'installation_command': 'pip install bookworm_genai'
  },
  {
    'library': 'ada-genai',
    'installation_command': 'pip install ada-genai'
  },
  ...{
    'library': 'semantix-genai-serve',
    'installation_command': 'pip install semantix-genai-serve'
  },
  {
    'library': 'platform-gen-ai',
    'installation_command': 'pip install platform-gen-ai'
  },
  
]
```

### Configuration Options

- **llm**: Defines the configuration for the LLM model, including the API key, model version, and endpoint.
- **verbose**: If set to `True`, enables detailed logging of operations.
- **headless**: If set to `True`, runs the web scraping in headless mode (without opening a browser window).
- **url**: The target URL for scraping.
- **prompt**: The natural language query to ask the LLM and fetch relevant content from the page.

Project Structure

---

The project is organized as follows: markdown Copy code

```markdown
├── README.md
├── scrapeAI/
│ ├── **init**.py
│ ├── core/
│ │ ├── **init**.py
│ │ ├── base_scraper.py
│ │ ├── direct_scraper.py
│ │ ├── scraper_factory.py
│ │ └── search_scraper.py
│ ├── llms/
│ │ ├── **init**.py
│ │ ├── anthropic_llm.py
│ │ ├── azure_openai_llm.py
│ │ ├── base.py
│ │ ├── google_llm.py
│ │ ├── llm_factory.py
│ │ └── openai_llm.py
│ ├── utils/
│ │ ├── **init**.py
│ │ ├── html_utils.py
│ │ └── logging.py
│ └── web_scraper.py
├── setup.py
├── tests/
│ └── tests_operations.py
```

### Core Components

- **core/**: Contains the base scraper classes and factory design patterns for scraping strategies.
- **llms/**: Includes different LLM integration classes such as OpenAI, Anthropic, and Google.
- **utils/**: Utility functions for HTML parsing and logging.

Contributing

---

We welcome contributions! If you'd like to improve the project, feel free to fork the repository and submit a pull request. Please follow the existing code structure and ensure that your contribution includes proper tests.

License

---

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Selenium Dependencies:

- Selenium requires browser drivers to interact with different browsers.
- The required driver for **Chrome** is **ChromeDriver**, and similarly, each browser has its respective driver.
- Make sure the driver is installed and placed in the system's PATH.

### Popular Browser Drivers:

- **Chrome**: [ChromeDriver](https://chromedriver.chromium.org/downloads)
- **Edge**: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Safari**: [WebDriver for Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)


<div style="text-align: center;">
  <a href="https://github.com/deBUGger404" target="_blank">
    <img src="https://raw.githubusercontent.com/deBUGger404/Python-Course-From-Beginner-to-Expert/main/Data/happy_code.webp" alt="Happy Code" style="width:200px; border-radius:12px;">
  </a>
</div>
