from selenium.webdriver.common.by import By


class LogInPage:

    text_username_id="user-name"
    text_password_id="password"
    btn_LogIn_id="login-button"
    title_product_xpath='//span[@class="title"]'
    menu_Button_xpath='//button[text()="Open Menu"]'
    common_xpath='//nav[@class="bm-item-list"]/a'
    logout_sidebar_link_XPATH ='//a[text()="Logout"]'


    def __init__(self,driver):
        self.driver=driver

    def getUserName(self,userName):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(userName)

    def getPassword(self, passWord):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(passWord)

    def getLoginButton(self):
        self.driver.find_element(By.ID, self.btn_LogIn_id).click()

    def getTitle(self):
        act_title=self.driver.find_element(By.XPATH, self.title_product_xpath).text
        return act_title

    def getMenu(self):
        self.driver.find_element(By.XPATH,self.menu_Button_xpath).click()

    def getLogout(self):
        self.driver.find_element(By.XPATH,self.logout_sidebar_link_XPATH).click()

    # def getLogOutButton(self,logOut="Logout"):
    #     all_item=self.driver.find_elements(By.XPATH, self.common_xpath)
    #     for item in all_item:
    #         if item.text==logOut:
    #             item.click()




