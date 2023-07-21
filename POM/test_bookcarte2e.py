from playwright.sync_api import sync_playwright

from pageObjects.bookCartLoginPage import LoginPageBK

def test_register_bk_user(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    login_bk.navigate_to_url()
    login_bk.clickRegisterLink()
    login_bk.fillRegistrationForm("Tamas", "Shud", "uesr", "Pass123$", "Pass123$", "m")
    login_bk.verify_registration_success()

def test_bk_login_with_valid_user(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    page.screenshot(path="POMexample.png")
    
def test_bk_login_with_invalid_user(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234xxxx")
    login_bk.verify_login_unsucess("Username or Password is incorrect.")
    page.screenshot(path="POMexample.png")
    print(page.title())
    
def test_logout_bk_user(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.logout_user()
    login_bk.verify_logout_success()
    
    
    
        
        

     
        