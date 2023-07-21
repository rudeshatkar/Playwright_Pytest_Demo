from playwright.sync_api import sync_playwright, expect


class SearchBook:

     def __init__(self, page):
        self.page = page
        self.search_box = page.locator("//input[@aria-label='search']")
        self.search_suggestion = page.locator(".cdk-overlay-container span.mat-option-text")
        self.book_card_title = page.locator(".card-title a strong")
        self.book_title = page.locator(".table tr:nth-child(1) td:nth-child(2)")
        self.book_auther = page.locator(".table tr:nth-child(2) td:nth-child(2)")
        self.clear_search_btn = page.locator("")
        
      
     def search_a_book(self, bookname):
         self.search_box.fill(bookname)
         
     def click_suggestion(self):    
         self.search_suggestion.click()
         
     def verify_search_result(self, bookname):
         expect(self.book_card_title).to_have_text(bookname)
         
     def verify_search_suggestion(self, bookname):
         expect(self.search_suggestion).to_contain_text(bookname)  
         
     def verify_no_suggestion(self):
         expect(self.search_suggestion).not_to_be_visible()    
         
     def verify_book_auther_title(self,auther, title):
         self.book_card_title.click()
         expect(self.book_auther).to_have_text(auther)
         expect(self.book_title).to_have_text(title)
         
         
             
         
             
             