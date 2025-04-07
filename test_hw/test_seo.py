from pages.demoqa import DemoQa
from pages.alerts import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
import pytest
import time
from conftest import browser

def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'

