from playwright.sync_api import sync_playwright
from pageObjects.filterPage import FilterPage
from pageObjects.loginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.addToCartPage import AddToCartPage


def test_login_with_standard_user(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    page.screenshot(path="POMexample.png")
    print(page.title())
    
def test_login_with_invalid_user(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    login_p.user_Login("standard_userxxx", "secret_saucexxx")
    login_p.verify_login_unsucess("Epic sadface: Username and password do not match any user in this service")
    page.screenshot(path="POMexample.png")
    
def test_login_with_blank_cred(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    login_p.user_Login("", "")
    login_p.verify_login_unsucess("Epic sadface: Username is required")
    page.screenshot(path="POMexample.png")
    
def test_login_and_logout(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    page.screenshot(path="POMexample.png")
    print(page.title())
    login_p.logout_user()
    login_p.verify_logout_success()    
    
def test_add_item_to_cart(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    cart_p.select_an_item()
    cart_p.verify_cart_count('1')
    page.screenshot(path="cart_inc.png")    
    
def test_remove_item_from_cart(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    page.screenshot(path="POMexample.png")
    print(page.title())
    cart_p.select_an_item()
    cart_p.remove_from_cart()
    page.screenshot(path="cart_inc.png")  
    
def test_remove_multi_item_from_cart(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    checkout_p = CheckoutPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    page.screenshot(path="POMexample.png")
    print(page.title())
    cart_p.select_multiple_item()
    cart_p.verify_cart_count('4')
    cart_p.remove_multiple_from_cart()
    page.screenshot(path="cart_empty.png")   
    
def test_verify_quantity_count(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    checkout_p = CheckoutPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    cart_p.select_an_item()
    cart_p.verify_cart_count('1')
    checkout_p.open_cart()
    checkout_p.verify_quantity('1')
    page.screenshot(path="cart_qty.png")  
                  
def test_verify_price_currency(set_up_tear_down): 
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    checkout_p = CheckoutPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    cart_p.select_an_item()
    cart_p.verify_cart_count('1')
    checkout_p.open_cart()
    checkout_p.verify_currency('$')
    page.screenshot(path="cart_qty.png")  
        
def test_checkout_shoping_to_finish(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    cart_p = AddToCartPage(page)
    checkout_p = CheckoutPage(page)
    cart_p = AddToCartPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    # import pdb; pdb.set_trace()
    cart_p.select_an_item()
    cart_p.verify_cart_count('1')
    page.screenshot(path="cart_inc.png")
    checkout_p.open_cart()
    checkout_p.checkout()
    checkout_p.enter_details('rude', 'rude', '12345')
    checkout_p.continue_checkout()
    checkout_p.finish_checkout("Thank you for your order!")
    checkout_p.back_to_home()
    
def test_filter_az_name(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    filter_p = FilterPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    filter_p.sort_name_filter("az")    
    filter_p.verify_name_filter_added("Sauce Labs Backpack")
    page.screenshot(path="atoz.png")
    
def test_filter_za_name(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    filter_p = FilterPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    # import pdb; pdb.set_trace()
    filter_p.sort_name_filter("za")  
    # filter_p.verify_name_filter_added("Test.allTheThings() T-Shirt (Red)")
    
    
def test_filter_lh_price(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    filter_p = FilterPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    filter_p.sort_price_filter("lohi")    
    # filter_p.verify_price_filter_added("7.99") 
    page.screenshot(path="ltoh.png")
    
def test_filter_hl_price(set_up_tear_down):
    browser = set_up_tear_down
    context = browser.new_context()
    page = context.new_page()
    login_p = LoginPage(page)
    filter_p = FilterPage(page)
    login_p.user_Login("standard_user", "secret_sauce")
    login_p.verify_login_sucess("Products")
    filter_p.sort_price_filter("hilo")    
    # filter_p.verify_price_filter_added("49.99") 
    page.screenshot(path="htol.png")    
            
    
    
    
        
    
    
    