from setuptools import setup, find_packages

setup(
    name='scrapeAI',
    version='0.3.0',
    description='A Python library to scrape web data using LLMs and Selenium',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rakesh Kumar',
    author_email='rakeshparmuwal1436@example.com',
    url='https://github.com/deBUGger404/Scrape-AI',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'anthropic',
        'openai',
        'google-generativeai'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
