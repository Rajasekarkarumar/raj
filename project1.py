from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import unittest
from pip._vendor.typing_extensions import Self

class LoginTest:

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        
        
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
    
    def test_Login_01_validLogin(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        username = 'Admin'
        password = 'admin123'
        username_input = self.driver.find_element(by=By.NAME, value='username')
        password_input = self.driver.find_element(by=By.NAME, value='password')
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       

        # send the username and password data to the input box respectively
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        signout_button = self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-userdropdown-name"]')
        signout_button.click()
        signOut=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-userdropdown-link"]')
        signOut.click()
        time.sleep(5)
        print('=============test_Login_01_validLogin==========')
        print('User able to successfully login HRmpage')
        
        self.driver.close()
        
    def test_Login_02_inValidLogin(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        username = 'Admin123'
        password = 'admin1234'
        username_input = self.driver.find_element(by=By.NAME, value='username')
        password_input = self.driver.find_element(by=By.NAME, value='password')
        time.sleep(2)
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        # send the username and password data to the input box respectively
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        time.sleep(4)
        print('==========test_Login_02_inValidLogin================= ')
        print('Invalid credentials')

    def test_PIM_01(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        username = 'Admin'
        password = 'admin123'
        username_input = self.driver.find_element(by=By.NAME, value='username')
        password_input = self.driver.find_element(by=By.NAME, value='password')
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        # send the username and password data to the input box respectively
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        
        print('User able to successfully login HRmpage')
        time.sleep(3)
        Select_PIM=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        Select_PIM.click()
        time.sleep(4)
        Add_Button=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        #action = ActionChains(self.driver)
        #action.click(on_element = Add_Button)
        #action.perform()
        Add_Button.click()
        firstName = 'ss'
        lastName = 'RR'
        employeeID='123';
        firstName_input = self.driver.find_element(by=By.NAME, value='firstName')
        lastName_input = self.driver.find_element(by=By.NAME, value='lastName')
        emp_ID=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        save_emp_details=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
        firstName_input.send_keys(firstName)
        lastName_input.send_keys(lastName)
        emp_ID.send_keys(employeeID)
        save_emp_details.click()
        time.sleep(4)
        signout_button = self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-userdropdown-name"]')
        signout_button.click()
        signOut=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-userdropdown-link"]')
        signOut.click()
        time.sleep(4)
        print('employee details successfully Added')
        
        self.driver.close()
        
    
   
    def test_PIM_02(self):
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        username = 'Admin'
        password = 'admin123'
        username_input = self.driver.find_element(by=By.NAME, value='username')
        password_input = self.driver.find_element(by=By.NAME, value='password')
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        # send the username and password data to the input box respectively
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        
        print('User able to successfully login HRmpage')
        time.sleep(3)
        Select_PIM=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        Select_PIM.click()
        time.sleep(4)
        edit=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-icon bi-pencil-fill"]')
        edit.click()
        time.sleep(4)   
        update_firstName_input = self.driver.find_element(by=By.NAME, value='firstName').send_keys('123')
        save_emp_details=self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]') 
        save_emp_details.click()
        time.sleep(4)
        print('Existing Employee Details are edited and saved successfully')
        
        self.driver.close()
        
    def test_PIM_03(self):
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        username = 'Admin'
        password = 'admin123'
        username_input = self.driver.find_element(by=By.NAME, value='username')
        password_input = self.driver.find_element(by=By.NAME, value='password')
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        # send the username and password data to the input box respectively
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        
        print('User able to successfully login HRmpage')
        time.sleep(3)
        Select_PIM=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        Select_PIM.click()
        time.sleep(4)
        delete=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[1]/i')
        delete.click()
        time.sleep(4)
        Delete_popup = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
        time.sleep(4) 
        print('succesfully deleted user details')
        
        self.driver.close()

        
s = LoginTest()
s.test_Login_01_validLogin()
s.test_Login_02_inValidLogin()
s.test_PIM_01()
s.test_PIM_02()
s.test_PIM_03()


        
