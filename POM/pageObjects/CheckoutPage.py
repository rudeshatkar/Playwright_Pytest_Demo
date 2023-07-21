from playwright.sync_api import sync_playwright, expect

class CheckoutPage : 
    def __init__(self, page):
        self.page = page
        self.item_list = page.locator(".cart_item")
        self.checkout_option = page.locator("#checkout")
        self.cart_option = page.locator("#shopping_cart_container")
        self.firstname_text = page.locator("#first-name")
        self.lastname_text = page.locator("#last-name")
        self.zip_text = page.locator("#postal-code")
        self.continue_option = page.locator("#continue")
        self.item_overview = page.locator("#header_container div span.title")
        self.finish_option = page.locator("#finish")
        self.checkout_confirm = page.locator("#checkout_complete_container h2")
        self.back_to_home_option = page.locator("#back-to-products")
        self.item_quantity = page.locator("#cart_contents_container div.cart_quantity")
        self.item_currency = page.locator(".cart_item_label div.inventory_item_price")
        
    def open_cart(self):
        self.cart_option.click()  
        expect(self.item_list).to_be_visible()
        
    def verify_quantity(self,qty) :
        expect(self.item_quantity).to_be_visible()
        expect(self.item_quantity).to_contain_text(qty)
        
    def verify_currency(self, currency):
        expect(self.item_currency).to_be_visible()
        expect(self.item_currency).to_contain_text(currency) 
        
    def checkout(self):    
        self.checkout_option.click()
        
    def enter_details(self,f_name, l_name,p_code):
        self.firstname_text.fill(f_name) 
        self.lastname_text.fill(l_name)
        self.zip_text.fill(p_code) 
        
    def continue_checkout(self) :
        self.continue_option.click()
        expect(self.item_overview).to_be_visible
        
    def finish_checkout(self, text) :
        self.finish_option.click()
        expect(self.checkout_confirm).to_be_visible()
        Thankyoumesssage = self.checkout_confirm.inner_text()   
        print(Thankyoumesssage)
        assert text in Thankyoumesssage 
        
    def back_to_home(self) :
        self.back_to_home_option.click()
            
        
         
        
    