from playwright.sync_api import sync_playwright
from pageObjects.cartPage import Cart
from pageObjects.bookCartLoginPage import LoginPageBK
from pageObjects.searchBookPage import SearchBook

def test_add_book_to_cart(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    search_bk = SearchBook(page)
    cart_bk = Cart(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    cart_bk.add_book_to_cart()
    # cart_bk.verify_cart_count("1")
    
def test_remove_book_from_cart(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    search_bk = SearchBook(page)
    cart_bk = Cart(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    cart_bk.add_book_to_cart()
    cart_bk.open_cart()
    cart_bk.remove_item_from_cart()
    # cart_bk.verify_cart_count("0")
    
def test_add_multiple_books_to_cart(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    cart_bk = Cart(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    cart_bk.add_multi_books_to_cart()
    # cart_bk.verify_cart_count("4")
    
def test_clear_cart(set_up_tear_down) :
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    cart_bk = Cart(page)
    search_bk = SearchBook(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    cart_bk.add_book_to_cart()
    cart_bk.open_cart()
    cart_bk.cart_clear() 
    cart_bk.verify_cart_count("0")
    
def test_incerase_quantity(set_up_tear_down) :
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    cart_bk = Cart(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    cart_bk.add_book_to_cart()
    cart_bk.open_cart()
    cart_bk.increase_book_quantity()
    # cart_bk.verify_cart_count("2")
    
    
        
    
    
    
     
        
    
    
     