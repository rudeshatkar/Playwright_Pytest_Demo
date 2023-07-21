from playwright.sync_api import sync_playwright

from pageObjects.bookCartLoginPage import LoginPageBK
from pageObjects.searchBookPage import SearchBook


def test_search_book(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    search_bk = SearchBook(page)
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    search_bk.verify_search_result("Robbie")
    
def test_partial_search_book(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    search_bk = SearchBook(page)
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("before")
    search_bk.verify_search_suggestion(" Before We Were Yours ")
        
def test_no_suggestion_for_invalid_search(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    search_bk = SearchBook(page)
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("_!Robbie")  
    search_bk.verify_no_suggestion()     
    
def test_search_by_auther(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    search_bk = SearchBook(page)
    login_bk = LoginPageBK(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Penelope Douglas")  
    search_bk.verify_search_suggestion("Birthday Girl")
    search_bk.click_suggestion()
    search_bk.verify_book_auther_title("Penelope Douglas", "Birthday Girl") 
    

      
        