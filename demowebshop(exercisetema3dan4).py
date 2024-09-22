import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class DemoWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # 1 positive Regist
    def test_1_Cek_URL_regist (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        get_url_regist = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/register', get_url_regist)

     # 2 positive Regist
    def test_2_Cek_tittle_regist (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        title_regist = driver.find_element(By.XPATH, "//h1[normalize-space()='Register']").text
        self.assertEqual("Register", title_regist)

     # 1 Negative Regist
    def test_3_Check_error_msg_regist_field_blank (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        
        error_msg_regist_firstname = driver.find_element(By.XPATH, "//span[@for='FirstName']").text
        self.assertEqual("First name is required.", error_msg_regist_firstname)

        error_msg_regist_lastname = driver.find_element(By.XPATH, "//span[@for='LastName']").text
        self.assertEqual("Last name is required.", error_msg_regist_lastname)

        error_msg_regist_email = driver.find_element(By.XPATH, "//span[@for='Email']").text
        self.assertEqual("Email is required.", error_msg_regist_email)

        error_msg_regist_pass = driver.find_element(By.XPATH, "//span[@for='Password']").text
        self.assertEqual("Password is required.", error_msg_regist_pass)

        error_msg_regist_conpass = driver.find_element(By.XPATH, "//span[@for='ConfirmPassword']").text
        self.assertEqual("Password is required.", error_msg_regist_conpass)

    # 2 Negative Regist
    def test_4_Check_error_msg_regist_wrong_email (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('a')
        driver.find_element(By.XPATH, "//input[@id='Password']").click()

        error_msg_regist_wrong_email = driver.find_element(By.XPATH, "//span[@for='Email']").text
        self.assertEqual("Wrong email", error_msg_regist_wrong_email)

    # 3 Negative Regist    
    def test_5_Check_error_msg_regist_pass_6char (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('b')
        driver.find_element(By.XPATH, "//input[@id='Email']").click()

        error_msg_regist_pass_6char = driver.find_element(By.XPATH, "//span[@for='Password']").text
        self.assertEqual("The password should have at least 6 characters.", error_msg_regist_pass_6char)

    # 4 Negative Regist 
    def test_6_Check_error_msg_regist_conpass_not_match (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('1234567')
        driver.find_element(By.XPATH, "//input[@id='Email']").click()

        error_msg_regist_conpass_not_match = driver.find_element(By.XPATH, "//span[@for='ConfirmPassword']").text
        self.assertEqual("The password and confirmation password do not match.", error_msg_regist_conpass_not_match)

    # 5 Negative Regist 
    def test_7_Check_error_msg_regist_email_already_exist (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys('wahyu')
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys('aws')
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('test@test.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()

        error_msg_regist_email_already_exist = driver.find_element(By.XPATH, "//li[normalize-space()='The specified email already exists']").text
        self.assertEqual("The specified email already exists", error_msg_regist_email_already_exist)

    # 3 positive Regist
    def test_8_Check_success_regist (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys('wahyu')
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys('aws')
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('wahyuaws321123@test.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()

        get_url_success_regist = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/registerresult/1', get_url_success_regist)

        text_success_login = driver.find_element(By.XPATH, "//div[@class='result']").text
        self.assertEqual("Your registration completed", text_success_login)

    # 1 positive Login
    def test_9_Check_URL_Login (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        get_url_login = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/login', get_url_login)

    # 2 positive Login
    def test_10_Check_tittle_Login (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        title_login = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome, Please Sign In!']").text
        self.assertEqual("Welcome, Please Sign In!", title_login)

    # 1 Negative Login
    def test_11_Check_error_msg_Login_email_pass_empty (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg_Login_general = driver.find_element(By.XPATH, "//span[contains(text(),'Login was unsuccessful. Please correct the errors ')]").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error_msg_Login_general)

        error_msg_Login_email_pass_empty = driver.find_element(By.XPATH, "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//ul/li[.='No customer account found']").text
        self.assertEqual("No customer account found", error_msg_Login_email_pass_empty)
        
    # 2 Negative Login
    def test_12_Check_error_msg_Login_email_No_cust_found (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('gaadausernyanih@mail.com')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg_Login_general = driver.find_element(By.XPATH, "//span[contains(text(),'Login was unsuccessful. Please correct the errors ')]").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error_msg_Login_general)

        error_msg_Login_acc_no_found = driver.find_element(By.XPATH, "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//ul/li[.='No customer account found']").text
        self.assertEqual("No customer account found", error_msg_Login_acc_no_found)

    # 3 Negative Login
    def test_13_Check_error_msg_Login_cust_deleted (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('aaa@aaa.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg_Login_general = driver.find_element(By.XPATH, "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']/div//form[@action='/login']//div[@class='validation-summary-errors']/span").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error_msg_Login_general)

        error_msg_Login_acc_deleted = driver.find_element(By.XPATH, "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//ul/li[.='Customer is deleted']").text
        self.assertEqual("Customer is deleted", error_msg_Login_acc_deleted)

    # 3 positive Login
    def test_14_Check_success_login (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        get_url_success_login = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/', get_url_success_login)

        email_logged = driver.find_element(By.XPATH, "//a[normalize-space()='wahyutest123@mail.com']").text
        self.assertEqual('wahyutest123@mail.com', email_logged)

    # 1 positive Shopping Cart - Checkout
    def test_15_notif_bar_success_add_to_cart (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.find_element(By.XPATH, "//div[@id='bar-notification']")

    # 2 positive Shopping Cart - Checkout
    def test_16_cart_page (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.find_element(By.XPATH, "//div[@id='bar-notification']")
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()
        
        get_url_cart = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/cart', get_url_cart)

    # 1 Negative Shopping Cart - Checkout
    def test_17_max_qty_on_cart (self):
       driver = self.driver
       driver.get("https://demowebshop.tricentis.com/")
       driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
       driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
       driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
       driver.find_element(By.XPATH, "//input[@value='Log in']").click()
       driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
       driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()
       driver.find_element(By.CLASS_NAME, "qty-input").clear()
       driver.find_element(By.CLASS_NAME, "qty-input").send_keys('100001')
       driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
        
       error_msg_max_qty = driver.find_element(By.XPATH, "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-1']//form[@action='/cart']/table[@class='cart']//ul/li[.='The maximum quantity allowed for purchase is 10000.']").text
       self.assertEqual('The maximum quantity allowed for purchase is 10000.', error_msg_max_qty)
   
    
    # 2 Negative Shopping Cart - Checkout
    def test_18_popup_agree_ToS (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click() 
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        popuperror_ToS = driver.find_element(By.XPATH, "//span[@id='ui-id-2']").text
        self.assertEqual('Terms of service', popuperror_ToS)

        copy_popuperror_ToS = driver.find_element(By.XPATH, "//p[contains(text(),'Please accept the terms of service before the next')]").text
        self.assertEqual('Please accept the terms of service before the next step.', copy_popuperror_ToS)

    # 3 positive Shopping Cart - Checkout
    def test_19_checkout_page (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click() 
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()
        driver.find_element(By.CLASS_NAME, "qty-input").clear()
        driver.find_element(By.CLASS_NAME, "qty-input").send_keys(1)
        driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
        driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        
        get_url_checkout = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/onepagecheckout', get_url_checkout)
        
        Heading_Chekcout = driver.find_element(By.XPATH, "//h1[normalize-space()='Checkout']").text
        self.assertEqual('Checkout', Heading_Chekcout)

    # 3 positive Shopping Cart - Checkout
    def test_20_success_checkout (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('wahyutest123@mail.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='master-wrapper-main']//div[4]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-72']").click()
        driver.implicitly_wait(100)    
        driver.find_element(By.XPATH, "//span[normalize-space()='Shopping cart']").click()  
        driver.find_element(By.CLASS_NAME, "qty-input").clear()
        driver.find_element(By.CLASS_NAME, "qty-input").send_keys(1)
        driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
        driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-method-next-step-button']").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-info-next-step-button']").click() 
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
        time.sleep(5)


        #cek URL success checkout
        get_url_success_checkout = driver.current_url
        self.assertEqual('https://demowebshop.tricentis.com/checkout/completed/', get_url_success_checkout)
     
        #cek heading success checkcout
        thankyou_text = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[1]/h1").text
        print(f"message yang diambil: {thankyou_text}")
        self.assertIn("Thank you", thankyou_text)  
        time.sleep(5)

        thankyou_text = driver.find_element(By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']").text
        print(f"message yang diambil: {thankyou_text}")
        self.assertIn("Your order has been successfully processed!", thankyou_text)  
        time.sleep(5)

        #continue to dashboard
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        















    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()