from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.implicitly_wait(5)  # ожидание действия в 5 секунд, если не нашелся selector
try:
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element_by_css_selector('#book').click()
    button = browser.find_element_by_css_selector('#solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x1 = browser.find_element_by_css_selector('#input_value').text
    y = calc(x1)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    button.click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    alert.accept()
    # авторизуемся на Степике
    browser.get('https://stepik.org/catalog?auth=login&language=ru')

    browser.find_element_by_id('id_login_email').send_keys('login')  # здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('password')  # здесь вводится пароль

    browser.find_element_by_class_name('sign-form__btn').click()
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')

    answer_input = browser.find_element_by_css_selector('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    browser.quit()