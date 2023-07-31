from playwright.sync_api import sync_playwright
from pageObjects.themesPage import Themes
from pageObjects.bookCartLoginPage import LoginPageBK

def test_theme_deep_purple_and_amber(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    theme_bk = Themes(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    theme_bk.click_theme_btn()
    theme_bk.select_theme_purple_amber()
    theme_bk.verify_theme('rgb(255, 215, 64)','rgb(103, 58, 183)')
    
def test_theme_indigo_and_pink(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    theme_bk = Themes(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    theme_bk.click_theme_btn()
    theme_bk.select_theme_indigo_pink()
    theme_bk.verify_theme("rgb(255, 64, 129)","rgb(63, 81, 181)")    
    
def test_theme_pink_and_blue_gray(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    theme_bk = Themes(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    theme_bk.click_theme_btn()
    theme_bk.select_theme_pink_ble_gray()
    theme_bk.verify_theme("rgb(176, 190, 197)","rgb(233, 30, 99)")    
    
def test_theme_purple_and_green(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    theme_bk = Themes(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    theme_bk.click_theme_btn()
    theme_bk.select_theme_purple_green()
    theme_bk.verify_theme("rgb(105, 240, 174)","rgb(156, 39, 176)")    
    