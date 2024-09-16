import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(Config.URL)
    yield firefox
    firefox.quit()






