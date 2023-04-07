from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options,
                              service=Service(ChromeDriverManager().install())
                              )
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    soup = bs(content, features='html.parser')
    return soup.get_text()
