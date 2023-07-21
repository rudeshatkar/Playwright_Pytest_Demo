
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import traceback
import pytest

options = Options()

@pytest.fixture()
def set_up_tear_down():
    try:
        cloud_url = "https://c466f7d1-7ab5-4213-a502-ca3e3ed6efed:Y2IyMDk4YTEzMjZhNDEwNzk1NjJhODZkMmYxNDJiNzc=@broadvoice-demo-org.cloudifytests.io/wd/hub"
        ns = cloud_url.split('@')
        name_space = ns[1].split('/')

        options = Options()
        options.headless = False

        options.browser_version = '107.0'
        cloud_options = {
            'name': 'Sauce Demo Set',
            'buildName': 'Sauce Lab',
            'enableLogs': True,
            'enableVideo': True,
            'deviceName': 'Desktop',
            'screenResolution': '1920x1080x24',
            'timeout': 1,
            'idleSessionTimeout': 1,
            'requestType': 'playwright',
            "enableProxy": False,
            "proxyName": ""
        }
        options.set_capability('cloudify:options', cloud_options)
        driver = webdriver.Remote(cloud_url, options=options)
        with sync_playwright() as p:
            cdp_url = "wss://" + name_space[0] + "/playwright/" + driver.session_id
            # cdp_url = "ws://tft.cloudifytests.io" + "/playwright/" + driver.session_id

            browser = p.chromium.connect(cdp_url)
            yield browser
            browser.close()
            driver.quit()
    except:
        traceback.print_exc()
        raise
    



######## Normal Run ########################################

# from playwright.sync_api import sync_playwright
# import pytest
# # import pdb; pdb.set_trace()
# @pytest.fixture(scope='module')
# def set_up_tear_down(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     yield page