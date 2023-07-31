from playwright.sync_api import sync_playwright, expect


class Themes:

    def __init__(self, page):
        self.page = page
        self.theme_picker = page.locator("//mat-icon[text()='format_color_fill']")
        self.deep_purple_and_amber = page.locator("(//button[contains(@class,'mat-focus-indicator mat-menu-item')])[1]")
        self.indigo_and_pink = page.locator("(//button[contains(@class,'mat-focus-indicator mat-menu-item')])[2]")
        self.pink_and_blue_gray = page.locator("(//button[contains(@class,'mat-focus-indicator mat-menu-item')])[3]")
        self.purple_and_green = page.locator("(//button[contains(@class,'mat-focus-indicator mat-menu-item')])[4]")
        self.color_one = page.locator("//div[@class='docs-example-viewer-title mat-elevation-z2']")
        self.color_two = page.locator("(//mat-card-content[@class='mat-card-content']//button)[1]")
        
    def click_theme_btn(self):
         self.theme_picker.click()
         
    def select_theme_purple_amber(self):
        self.deep_purple_and_amber.click()
        
    def select_theme_indigo_pink(self):
        self.indigo_and_pink.click()
        
    def select_theme_pink_ble_gray(self):
        self.pink_and_blue_gray.click()
        
    def select_theme_purple_green(self):
        self.purple_and_green.click()
        
    def verify_theme(self, col1, col2):
        expect(self.color_one).to_have_css("background-color", col1)
        expect(self.color_two).to_have_css("background-color", col2)                     
            
        
        