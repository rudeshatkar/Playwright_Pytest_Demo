from playwright.sync_api import sync_playwright, expect


class LoginPage:
    #  def __enter__(self):
    #     return "entered!"

     def __init__(self, page):
      #   page = context.new_page()
        self.page = page
        self.username_input_text = page.locator('#user-name')
        self.password_input_text = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.product_list = page.locator("#header_container span.title")
        self.error_msg = page.locator("#login_button_container h3")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_option = page.locator("#logout_sidebar_link")
        self.login_wrapper = page.locator(".login_wrapper-inner")
        
     def user_Login(self, u_name, u_pass):
         self.page.goto("https://www.saucedemo.com/")
         self.username_input_text.fill(u_name)
         self.password_input_text.fill(u_pass)
         self.login_button.click()
         


     def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

     def u_name(self, text):
        self.username_input_text.fill(text)
        
     def u_pass(self, text):
        self.password_input_text.fill(text)
     
     def login(self):
        self.login_button.click()
        
     def verify_login_sucess(self, text):
        expect(self.product_list).to_have_text(text) 
        
     def verify_login_unsucess(self, text):
        expect(self.error_msg).to_have_text(text) 
        
     def logout_user(self):
        self.burger_menu.click()
        self.logout_option.click()
    
     def verify_logout_success(self):
        expect(self.login_wrapper).to_be_visible()    
                    