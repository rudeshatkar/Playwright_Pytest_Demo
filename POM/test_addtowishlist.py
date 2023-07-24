from playwright.sync_api import sync_playwright
from pageObjects.addToWishlistPage import WishlistPage
from pageObjects.bookCartLoginPage import LoginPageBK
from pageObjects.searchBookPage import SearchBook

def test_add_book_to_wishlist(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    search_bk = SearchBook(page)
    wishlist_bk = WishlistPage(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    wishlist_bk.add_remove_book_to_wishlist()
    wishlist_bk.verify_wishlist_count("1")
    
def test_remove_book_from_wishlist(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    search_bk = SearchBook(page)
    wishlist_bk = WishlistPage(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    wishlist_bk.add_remove_book_to_wishlist()
    wishlist_bk.verify_wishlist_count("0")
    
def test_add_multiple_books_to_wishlist(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    wishlist_bk = WishlistPage(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    wishlist_bk.add_multi_books_to_wishlist()
    wishlist_bk.verify_wishlist_count("4")
    
def test_clear_wishlist(set_up_tear_down) :
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_bk = LoginPageBK(page)
    wishlist_bk = WishlistPage(page)
    search_bk = SearchBook(page)
    login_bk.user_Login("ortoni", "Pass1234")
    login_bk.verify_login_sucess()
    search_bk.search_a_book("Robbie")
    search_bk.click_suggestion()
    wishlist_bk.add_remove_book_to_wishlist()
    wishlist_bk.openWishlist()
    wishlist_bk.wishlist_clear() 
    wishlist_bk.verify_wishlist_count("0")
    
    
    
        
    
    
    
     
        
    
    
     