from playwright.sync_api import sync_playwright
from pageObjects.ordersPage import Orders
from pageObjects.cartPage import Cart
from pageObjects.bookCartLoginPage import LoginPageBK
from pageObjects.searchBookPage import SearchBook

def test_order_book(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    search_bk = SearchBook(page)
    cart_bk = Cart(page)
    order_bk = Orders(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    cart_bk.add_book_to_cart()
    cart_bk.open_cart()
    order_bk.click_to_checkout()
    order_bk.add_details("Tamam Turk", "Dehli", "South", "411422", "Delhli")
    order_bk.click_place_order()
    
def test_my_orders(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    order_bk = Orders(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    order_bk.open_my_orders()
    order_bk.verify_orders()
    
    
        
    
    

    
    