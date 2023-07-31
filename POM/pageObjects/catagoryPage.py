from playwright.sync_api import sync_playwright, expect


class Catagory:

     def __init__(self, page):
        self.page = page
        self.all_caatagory_btn = page.locator("//a[contains(text(),'All Categories')]")
        self.biography_btn = page.locator("(//div[@class='mat-list-item-content'])[2]")
        self.fiction_btn = page.locator("//a[contains(text(),'Fiction')]")
        self.mistry_btn = page.locator("//a[contains(text(),'Mystery')]")
        self.fantacy_btn = page.locator("//a[contains(text(),'Fantasy')]")
        self.romance_btn = page.locator("//a[contains(text(),'Romance')]")
        self.book_cover_list = page.locator(".mat-card-image.preview-image")
        self.book_cover = page.locator("(//img[@class='mat-card-image preview-image'])[1]")
        self.catagory_name = page.locator("//table[@class='table']/tr[3]/td[2]")
        # self.color = page.locator("//div[@class='docs-example-viewer-title mat-elevation-z2']")
        
        
     def verify_catagory_list_count(self, list):
        elements = (self.book_cover_list) 
        expect(elements).to_have_count(int(list))
        # expect(self.color).to_have_css('background','rgb(255, 64, 129)');

        
     def click_all_catagory(self):
         self.all_caatagory_btn.click()
         
     def click_biography_btn(self):
         self.biography_btn.click()
         
     def click_fiction_btn(self):
         self.fiction_btn.click()
         
     def click_mistery_btn(self):
         self.mistry_btn.click()
         
     def click_fancacy_btn(self):
         self.fantacy_btn.click()
         
     def click_romance_btn(self):
         self.romance_btn.click()                   
            
        
     def verify_ctagory(self, cat):
         self.book_cover.click()
         expect(self.catagory_name).to_have_text(cat)
         
            
        
            
    