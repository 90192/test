from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs


def get_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    service = Service('driver/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get(url)
    content = driver.execute_script('return document.body.innerHTML;')
    driver.quit()
    soup = bs(content, features='html.parser')
    return soup.get_text()
