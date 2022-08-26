Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium) 
in the process of testing the (https://www.labirint.ru) site



Files
-----

[conftest.py](conftest.py) contains all the required code (fixtures) to run tests and log in personal cabinet.

[constants.py](constants.py) contains all needed data for performing tests and also some messages from some pages

[pages/app.py](pages/app.py) helper class that contains information about driver, url and also all pages 

[pages/base_page.py](pages/base_page.py) contains PageObject pattern implementation for Python (implementation main methods of webdriver)

[pages/login_page.py](pages/login_page.py) contains PageObject pattern implementation for performing tests related with "log in" actions and also contain locators
to define web elements on web pages.

[pages/main_page.py](pages/main_page.py) contains PageObject pattern implementation for performing tests related with all actions on the main page and also contain locators
to define web elements on web pages.


[tests/test.py](tests/test.py) contains all Web UI tests for Labirint (https://www.labirint.ru)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```


Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
