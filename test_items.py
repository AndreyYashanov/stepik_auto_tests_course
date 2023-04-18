import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_exists(browser):
    print('\nOpening page in {}...'.format(browser.name))
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_cart_button is not None, 'Add to cart button not found'
