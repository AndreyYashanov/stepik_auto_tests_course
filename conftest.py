import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser')
    browser = None

    if browser_name == 'chrome':
        print('\nStarting Chrome browser...')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nStarting Firefox browser...')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')

    yield browser
    print('\nQuitting browser...')
    browser.quit()
