from playwright.sync_api import sync_playwright, expect

class AddToCartPage:
    def __init__(self, page):
        self.page = page
        self.cart_btn = page.locator(".shopping_cart_link")
        self.add_item_tothe_cart = page.locator("#add-to-cart-sauce-labs-backpack")
        self.add_item_light = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.add_item_tshirt = page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_item_jacket = page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        self.remove_item = page.locator("#remove-sauce-labs-backpack")
        self.remove_light = page.locator("#remove-sauce-labs-bike-light")
        self.remove_tshirt = page.locator("#remove-sauce-labs-bolt-t-shirt")
        self.remove_jacket = page.locator("#remove-sauce-labs-fleece-jacket")
        self.cart_count = page.locator(".shopping_cart_link span")
        self.cart_option = page.locator("#shopping_cart_container")
        self.remove_optiom = page.locator("#remove-sauce-labs-backpack")
        self.checkout_option = page.locator("#checkout")
    
    def select_an_item(self):
        # if(expect(self.add_item_tothe_cart).to_be_visible() == True):
            self.add_item_tothe_cart.click()
        # else:
        #     self.remove_item.click()
        #     self.add_item_tothe_cart.click()   
        
    def select_multiple_item(self):
        self.add_item_tothe_cart.click()  
        self.add_item_light.click()
        self.add_item_tshirt.click()
        self.add_item_jacket.click()         
      
    def remove_from_cart(self):
        self.remove_item.click()
     
    def remove_multiple_from_cart(self):
        self.cart_btn.click()
        self.remove_item.click() 
        self.remove_light.click()
        self.remove_tshirt.click()
        self.remove_jacket.click()    
         
    def verify_cart_count(self,count):
        expect(self.cart_count).to_have_text(count)
        
    def remove_cart_item(self):
        self.cart_option.click()
        self.remove_optiom.click()
        expect(self.checkout_option).to_be_visible()
        