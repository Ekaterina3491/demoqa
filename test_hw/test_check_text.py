from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_footer.get_text() =='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_text_center(browser):
    demo_qa_page = DemoQa(browser)
    elem_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elem_page.text_center.get_text() == 'Please select an item from left to start practice.'
