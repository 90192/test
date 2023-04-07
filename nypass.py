from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import tempfile


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    with tempfile.TemporaryDirectory() as tmp:
        driver_path = ChromeDriverManager(cache_path=tmp).install()
        driver = webdriver.Chrome(driver_path, options=options)
    # driver = webdriver.Chrome(options=options,
    #                           service=Service(ChromeDriverManager().install())
    #                           )
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    soup = bs(content, features='html.parser')
    return soup.get_text()
