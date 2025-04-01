import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()


@pytest.fixture()
def driver():
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options=options)
    _driver.get(os.getenv("WEBSITE_URL"))
    yield _driver
    _driver.quit()
