from playwright.sync_api import sync_playwright, expect


class Orders:

     def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("//span[text()='CheckOut']")
        self.checkout_input_name = page.locator("//input[@data-placeholder='Name']")
        self.checkout_input_address_one = page.locator("//input[@data-placeholder='Address Line 1']")
        self.checkout_input_address_two = page.locator("//input[@data-placeholder='Address Line 2']")
        self.checkout_pincode = page.locator("//input[@data-placeholder='Pincode']")
        self.checkout_state = page.locator("//input[@data-placeholder='State']")
        self.checkout_place_order = page.locator("//span[text()='Place Order']")
        self.order_header = page.locator("//h2[text()='My Orders']")
        self.my_order_btn = page.locator("//button[text()='My Orders']")
        self.profile_icon_btn = page.locator("//mat-icon[text()='arrow_drop_down']")
        self.order_Id = page.locator("(//tr[1][contains(@class,'mat-row cdk-row')]//td)[1]")
        self.order_details = page.locator("//table[contains(@class,'table tbl-orderdetails')]")
        self.order_page = page.locator("//h2[text()='My Orders']")
        
        
        
     def click_to_checkout(self):
        self.checkout_button.click()    
        
     def add_details(self, name, addr1, addr2, pin, state):
         self.checkout_input_name.fill(name)
         self.checkout_input_address_one.fill(addr1)
         self.checkout_input_address_two.fill(addr2)
         self.checkout_pincode.fill(pin)
         self.checkout_state.fill(state)
      
     def click_place_order(self):
         self.checkout_place_order.click()
         expect(self.order_header).to_be_visible()
         
     def open_my_orders(self):
        self.profile_icon_btn.click()
        self.my_order_btn.click()
        
     def verify_orders(self):
      #   self.order_Id.click()
      #   expect(self.order_details).to_be_visible()
        expect(self.order_page).to_be_visible()
        
        
      
             
             
         
         
            
        
        