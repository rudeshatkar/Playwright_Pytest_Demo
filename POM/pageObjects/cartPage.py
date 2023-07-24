from playwright.sync_api import sync_playwright, expect


class Cart:

     def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = page.locator("(//button[@color='primary']//span)[1]")
        self.cart_count = page.locator("(//span[@class='mat-badge-content mat-badge-active'])[2]")
        self.cart_btn = page.locator("(//mat-icon[@data-mat-icon-type='font'])[3]")
        self.remove_item_btn = page.locator("(//mat-icon[text()='delete'])[1]")
        self.add_to_cart_btn_1 = page.locator("(//button[@color='primary'])[1]")
        self.add_to_cart_btn_2 = page.locator("(//button[@color='primary'])[2]")
        self.add_to_cart_btn_3 = page.locator("(//button[@color='primary'])[3]")
        self.add_to_cart_btn_4 = page.locator("(//button[@color='primary'])[4]")
        self.cart_clear_btn = page.locator("//div[@class='ng-star-inserted']//button[1]")
        self.increase_qty_btn = page.locator("(//mat-icon[text()='add_circle'])[1]")
        self.home_logo = page.locator("(//span[@class='mat-button-wrapper'])[1]")
        self.continue_shopping = page.locator("//span[text()='Continue shopping']")
        
        
     def add_book_to_cart(self):
         self.add_to_cart_btn.click()
         
     def add_multi_books_to_cart(self):
         self.add_to_cart_btn_1.click()
         self.add_to_cart_btn_2.click()
         self.add_to_cart_btn_3.click()
         self.add_to_cart_btn_4.click()
             
     def verify_cart_count(self, count):
         expect(self.cart_count).to_contain_text(count)
         
     def open_cart(self):
         self.cart_btn.click()    
         
     def remove_item_from_cart(self):
         self.remove_item_btn.click()
         
     def cart_clear(self):
         self.cart_clear_btn.click()
         
     def increase_book_quantity(self): 
         self.increase_qty_btn.click()
    
     def set_cart_zero(self,count):
         self.add_to_cart_btn.click()
         self.cart_btn.click()
         self.cart_clear_btn.click()
         expect(self.continue_shopping).to_be_visible()
         expect(self.cart_count).to_contain_text(count)
         self.page.reload()
         self.home_logo.click()
        #  ele = self.cart_clear_btn
        #  if(expect(self.cart_clear_btn).to_be_visible()):
        #     self.cart_clear_btn.click()
        #     self.home_logo.click()
        #  else:
        #     self.home_logo.click()   
        
  
         
                  
         
             
              
            