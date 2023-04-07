from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(executable_path='driver/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    soup = bs(content, features='html.parser')
    return soup.get_text()
