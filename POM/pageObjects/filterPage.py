from playwright.sync_api import sync_playwright, expect

class FilterPage : 
    def __init__(self, page):
        self.page = page
        self.filter_sort = page.locator(".product_sort_container")
        self.filter_options = page.locator("[data-test=\'product_sort_container\']")
        self.filter_name_atoz = page.locator("//option[text()='Name (A to Z)']") 
        self.filter_name_ztoa = page.locator("//option[text()='Name (Z to A)']") 
        self.filter_price_ltoh = page.locator("//option[text()='Price (low to high)']]") 
        self.filter_price_htol = page.locator("//option[text()='Price (high to low)']") 
        self.product_name = page.locator("(//div[@class='inventory_item_name'])[1]")
        self.product_price = page.locator("(//div[@class='inventory_item_price'])[1]")
        
    def sort_name_filter(self,val):
        # self.filter_sort.click()
        self.filter_sort.select_option(val)

        # self.filter_name_atoz.click()
        
    # def sort_filter_z_to_a(self):
    #     self.filter_sort.click()
    #     self.filter_name_ztoa.click() 
        
    def sort_price_filter(self,val):
        # self.filter_sort.click()
        self.filter_sort.select_option(val)
        
    # def sort_price_h_to_l(self):
    #     self.filter_sort.click()
    #     self.filter_price_htol.click()  
        
    def verify_name_filter_added(self,text):
        expect(self.product_name).to_contain_text(text)
        
    def verify_price_filter_added(self,text):
        expect(self.product_price).to_contain_text(text)    
                   
        
          
        
        
            