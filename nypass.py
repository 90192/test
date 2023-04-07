from selenium import webdriver
from bs4 import BeautifulSoup as bs


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    soup = bs(content, features='html.parser')
    return soup.get_text()
