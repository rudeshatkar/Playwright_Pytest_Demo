from playwright.sync_api import sync_playwright, expect

class WishlistPage:
    def __init__(self, page):
        self.page = page
        self.add_to_wishlist_btn = page.locator("(//span[text()=' favorite '])[1]")
        self.wishlist_count = page.locator("(//mat-icon[@data-mat-icon-type='font']//span)[1]")
        self.add_to_wishlist_btn1 = page.locator("(//div[contains(@class,'favourite mat-elevation-z4')]//span)[1]")
        self.add_to_wishlist_btn2 = page.locator("(//div[contains(@class,'favourite mat-elevation-z4')]//span)[2]")
        self.add_to_wishlist_btn3 = page.locator("(//div[contains(@class,'favourite mat-elevation-z4')]//span)[3]")
        self.add_to_wishlist_btn4 = page.locator("(//div[contains(@class,'favourite mat-elevation-z4')]//span)[4]")
        self.wishlist_btn = page.locator("//mat-icon[text()='favorite']")  
        self.clear_wishlist_btn = page.locator("//div[@class='ng-star-inserted']//button[1]")     
        
        
        
    def add_remove_book_to_wishlist(self): 
        self.add_to_wishlist_btn.click()
        
    def verify_wishlist_count(self,count):
        expect(self.wishlist_count).to_contain_text(count)
        
    def add_multi_books_to_wishlist(self):
         self.add_to_wishlist_btn1.click()
         self.add_to_wishlist_btn2.click()
         self.add_to_wishlist_btn3.click()
         self.add_to_wishlist_btn4.click()    
               
               
    def openWishlist(self):
        self.wishlist_btn.click() 
           
    def wishlist_clear(self):
        self.clear_wishlist_btn.click()
                   