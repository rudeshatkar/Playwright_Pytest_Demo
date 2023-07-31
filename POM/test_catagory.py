from playwright.sync_api import sync_playwright
from pageObjects.catagoryPage import Catagory
from pageObjects.cartPage import Cart
from pageObjects.bookCartLoginPage import LoginPageBK
from pageObjects.searchBookPage import SearchBook

def test_catagory_all_catagory(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_all_catagory()
    catagory_bk.verify_catagory_list_count("45")
    
    
def test_catagory_biography(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_biography_btn()
    catagory_bk.verify_catagory_list_count("9") 
    catagory_bk.verify_ctagory("Biography")   
    
def test_catagory_fiction(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_fiction_btn()
    catagory_bk.verify_catagory_list_count("10") 
    catagory_bk.verify_ctagory("Fiction")   
    
def test_catagory_mistery(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_mistery_btn()
    catagory_bk.verify_catagory_list_count("8")  
    catagory_bk.verify_ctagory("Mystery") 
    
def test_catagory_fantacy(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_fancacy_btn()
    catagory_bk.verify_catagory_list_count("8") 
    catagory_bk.verify_ctagory("Fantasy")
    
def test_catagory_romance(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    catagory_bk = Catagory(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    catagory_bk.click_romance_btn()
    catagory_bk.verify_catagory_list_count("10")  
    catagory_bk.verify_ctagory("Romance")                    
    