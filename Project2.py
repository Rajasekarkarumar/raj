from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

    def logout(self):
        self.driver.get(self.url)
        time.sleep(5)
        # For Login
        self.driver.find_element(by=By.NAME, value=self.input_box_username).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.input_box_password).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.login_xpath).click()
        # For Logout
        time.sleep(4)
        logout_button = self.driver.find_element(by=By.XPATH, value=self.logout_1)
        action = ActionChains(self.driver)
        action.click(on_element=logout_button)
        action.perform()
        time.sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()   

    def test_Search_1(self):
        
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
        time.sleep(2)
        search_Admin1 = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        #searchItem = ['Admin', 'PIM', 'Leave', 'Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Buzz']
        search_Admin1.send_keys('Admin')
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        time.sleep(3)

        search_Buzz = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Buzz.send_keys('Buzz')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()

        search_PIM = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_PIM.send_keys('PIM')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        time.sleep(2)
        search_Leave = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Leave.send_keys('Leave')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        time.sleep(2)   
        search_Time = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Time.send_keys('Time')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        time.sleep(2)
        search_Recruitment = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Recruitment.send_keys('Recruitment')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()

        time.sleep(2)
        search_MyInfo = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_MyInfo.send_keys('My Info')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click() 
        
        time.sleep(2)
        search_Performance = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Performance.send_keys('Performance')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        
        time.sleep(2)
        search_Dashboard = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Dashboard.send_keys('Dashboard')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        
        time.sleep(2)
        search_Directory = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Directory.send_keys('Directory')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        
        time.sleep(2)
        search_Maintenance = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        search_Maintenance.send_keys('Maintenance')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        
        time.sleep(2)
        #search_Buzz = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        #search_Buzz.send_keys('Buzz')
        #time.sleep(2)
        #self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
	    
        self.driver.close()

    def test_Admin_2(self):
        
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
        time.sleep(2)
        search_Admin1 = self.driver.find_element(by=By.XPATH, value='//input[@class="oxd-input oxd-input--active"]') 
        #searchItem = ['Admin', 'PIM', 'Leave', 'Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Buzz']
        search_Admin1.send_keys('Admin')
        self.driver.find_element(by=By.XPATH, value='//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a').click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
        time.sleep(2)
	    
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
       
        Create_Login_Details=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys('Admin2376')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys('Admin207#')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys('Admin207#')
        time.sleep(3)
        save_emp_details.click()
        time.sleep(3)
    
        self.driver.close()
    
    def test_PIM_04(self):
        
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        personal_details=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6')
        print(personal_details.is_displayed())
        Contact_Details=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a')
        print(Contact_Details.is_displayed())
        Emergency_Contacts=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a')
        print(Emergency_Contacts.is_displayed())
        Dependents=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a')
        print(Dependents.is_displayed())
        Immigration=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a')
        print(Immigration.is_displayed())
        job=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a')
        print(job.is_displayed())
        Salary=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a')
        print(Salary.is_displayed())
        Tax_Exemptions=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a')
        print(Tax_Exemptions.is_displayed())
        Report=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a')
        print(Report.is_displayed())
        Qualifications=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a')
        print(Qualifications.is_displayed())
        Memberships=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a')
        print(Memberships.is_displayed())
        
        time.sleep(4)
        
        self.driver.close()

          
    def test_PIM_05(self):
        
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        personal_details=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
        print(personal_details.is_displayed())
        personal_details.click()
        time.sleep(4)
        update_nickName=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')
        update_nickName.click()
        update_nickName.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        nickName='i'
        update_nickName.send_keys(nickName)
        time.sleep(4)
        save=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        time.sleep(4)
        nickNameText=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')
        
        print(nickNameText.get_attribute('value'))
        if nickName == nickNameText.get_attribute('value'):
            
            nickNameText.is_displayed()
            print("nick name is updated ")
        
        else:
        
            print("nick name is not updated ")
            
        time.sleep(4)

        self.driver.close()

    def test_PIM_06(self):
        
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        Contact_Details=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a')
        print(Contact_Details.is_displayed())
        Contact_Details.click()
        time.sleep(4)
        update_mobileno=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
        update_mobileno.click()
        update_mobileno.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        mobileno='1'
        update_mobileno.send_keys(mobileno)
        time.sleep(4)
        save=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
        time.sleep(4)
        mobilenoText=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input') 
        print(mobilenoText.get_attribute('value'))
        if mobileno == mobilenoText.get_attribute('value'):
            
            mobilenoText.is_displayed()
            print("mobilenoText is updated ")
        
        else:
        
            print("mobilenoText is not updated ")
            
        time.sleep(4)

        self.driver.close()


    def test_PIM_07(self):
        
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        Emergency_Contacts=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a')
        print(Emergency_Contacts.is_displayed())
        Emergency_Contacts.click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('S')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('K')
        update_EMmobileno=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
        update_EMmobileno.click()
        update_EMmobileno.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        EMmobileno='5'
        update_EMmobileno.send_keys(EMmobileno)
        time.sleep(4)
        save=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]').click()
        time.sleep(4)
        EMmobilenoText=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[5]/div') 
        print(EMmobilenoText.get_attribute('value'))
        if EMmobileno == EMmobilenoText.get_attribute('value'):
            
            EMmobilenoText.is_displayed()
            print("Emergency mobilenoText is updated ")
        
        else:
        
            print("Emergency mobilenoText is not updated ")
            
        time.sleep(4)

        self.driver.close()

    def test_PIM_08(self):
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
        self.driver.delete_all_cookies()
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #self.driver.implicitly_wait(10)
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        Dependents=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a')
        print(Dependents.is_displayed())
        Dependents.click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
        
        
        update_dependent=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
        update_dependent.click()
        update_dependent.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        dependentName='R'
        update_dependent.send_keys(dependentName)
    
        x=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
        #self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
        drop=Select(x)
        
        drop.select_by_visible_text("Child")
        time.sleep(4)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
        time.sleep(4)
        save=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]').click()
        time.sleep(4)
        dependentText=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[5]/div') 
        print(dependentText.get_attribute('value'))
        if dependentName == dependentText.get_attribute('value'):
            
            dependentText.is_displayed()
            print("dependent is updated ")
        
        else:
        
            print("dependent is not updated ")
            
        time.sleep(4)

        self.driver.close()
        
        
    def test_PIM_09(self):
        
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
        
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        job=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a')
        print(job.is_displayed())
        job.click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span').click()
        time.sleep(4)

        start_date='2023-05-02'
        end_date='2023-05-18'
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input').send_keys(start_date)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input').send_keys(end_date)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        time.sleep(4)     

        self.driver.close()
        
    def test_PIM_12(self):
        
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
        Select_employee_list=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]').click()
        time.sleep(4)
        Salary=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a')
        print(Salary.is_displayed())
        Salary.click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('S')
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div').click()
        time.sleep(10)
        
        Actions=ActionChains(self.driver)
        
        ele=self.driver.find_element(by=By.XPATH, value='//div[contains(text(),"Grade C"")]')
        
       
        
        Actions.move_to_element(ele)
       
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        
        time.sleep(4)

        self.driver.close()



s = LoginTest()

s.test_Search_1()
s.test_Admin_2()
s.test_PIM_03()
s.test_PIM_04()
s.test_PIM_05()
s.test_PIM_06()
s.test_PIM_07()
#s.test_PIM_08()
s.test_PIM_09()
s.test_PIM_12()