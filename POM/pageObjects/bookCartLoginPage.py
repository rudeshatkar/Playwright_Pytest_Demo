from playwright.sync_api import sync_playwright, expect


class LoginPageBK:
    #  def __enter__(self):
    #     return "entered!"

     def __init__(self, page):
      #   page = context.new_page()
        self.page = page
        self.username_input = page.locator("//input[@data-placeholder='Username']")
        self.password_input = page.locator("input[data-placeholder='Password']")
        self.login_btn = page.locator("button[color='primary']")
        self.product_list = page.locator("#header_container span.title")
        self.error_msg = page.locator("//mat-error[@class='mat-error ng-star-inserted']")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_option = page.locator("div#mat-menu-panel-1>div>button:nth-of-type(2)")
        self.login_profile_icon = page.locator("//mat-icon[text()='account_circle']")
        self.login_wrapper = page.locator(".docs-example-viewer-title-spacer")
     #  Registration Page
        self.registerLink = page.locator("//span[text()='Register']")
        self.firstName = page.locator("//input[@data-placeholder='First name']")
        self.lastName = page.locator("input[formcontrolname='lastname']")
        self.userName = page.locator("input[data-placeholder='User Name']")
        self.password = page.locator("input[data-placeholder='Password']")
        self.confirmPass = page.locator("input[data-placeholder='Confirm Password']")
        self.genderMaleButton = page.locator("(//span[@class='mat-radio-outer-circle'])[1]")
        self.genderFemaleButton= page.locator("(//span[@class='mat-radio-outer-circle'])[2]")
        self.confirmRegistration = page.locator("//span[text()='Register']")
        self.loginButton = page.locator("(//span[@class='mat-button-wrapper'])[3]") 
        
     def navigate_to_url(self):
         self.page.goto("https://bookcart.azurewebsites.net/login")
     
     def user_Login(self, u_name, u_pass):
         self.page.goto("https://bookcart.azurewebsites.net/login")
         self.username_input.fill(u_name)
         self.password_input.fill(u_pass)
         self.login_btn.click()
         
     def verify_login_sucess(self):
        expect(self.login_profile_icon).to_be_visible()  
        
     def verify_login_unsucess(self, text):
        expect(self.error_msg).to_have_text(text) 
        
     def logout_user(self):
        self.login_profile_icon.click()
        self.logout_option.click()
    
     def verify_logout_success(self):
        expect(self.login_wrapper).to_be_visible() 
        
     def verify_registration_success(self):
        expect(self.login_wrapper).to_be_visible()    
        
     def clickRegisterLink(self):
        self.registerLink.click()
        
     def fillRegistrationForm(self, firstName, lastName, userName, password, confirmPass, gender):
         self.firstName.fill(firstName)
         self.lastName.fill(lastName)
         self.userName.fill(userName)
         self.password.fill(password)
         self.confirmPass.fill(confirmPass)
         if (gender == "m"):
             self.genderMaleButton.click()
             expect(self.genderMaleButton).to_be_checked()
         else:
             self.genderFemaleButton.click()
             expect(self.genderFemaleButton).to_be_checked()
         self.confirmRegistration.click()    
           
                    