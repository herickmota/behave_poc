from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--windows-size=1024,768")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)


def after_all(context):
    context.driver.quit()
