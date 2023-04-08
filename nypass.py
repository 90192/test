from selenium import webdriver
from bs4 import BeautifulSoup as bs


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path='driver/chromedriver', options=options)
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    soup = bs(content, features='html.parser')
    return soup.get_text()
