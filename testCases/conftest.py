# conftest.py or your test setup file

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome()
    driver.get(ReadConfig.get_AdminURL())
    request.cls.driver = driver
    yield driver
    driver.quit()





'''

# conftest.py
import json
import os
from os import listdir


import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

@pytest.fixture(scope="session")
def driver(request):
    # admin_page_url = ReadConfig.get_AdminURL()
    driver = webdriver.Chrome()  # Initialize webdriver
    driver.get("http://10.106.100.222:9098/Chemia/login/cpl")  # Open
    yield driver

@pytest.fixture(scope="class")
def setUp(request, driver):
    request.cls.driver = driver
    yield driver
'''


'''

import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    driver=webdriver.Chrome()
    return driver


'''


'''
def pytest_addoption(parser):
    parser.addoption("--browser",actions="store",default="chrome",help="specify the browser:chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setUp(browser):
    global driver
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        raise ValueError("unsupported browser")
    return driver

'''


