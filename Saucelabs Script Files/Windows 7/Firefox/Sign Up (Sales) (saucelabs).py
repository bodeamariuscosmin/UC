import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from random import random
from random import randint
import random as rn
import unittest, time, re
my_string = 'string'


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '26'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Sign Up (Sales)'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"

    def test_sign_up_sales(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_css_selector("#please-sign-in > footer > p > a").click()
        driver.find_element_by_name("first").clear()
        driver.find_element_by_name("first").send_keys("qa")
        driver.find_element_by_name("last").clear()
        driver.find_element_by_name("last").send_keys("test")
        driver.find_element_by_xpath("(//input[@name='email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("parola")
        driver.find_element_by_css_selector("#sign-up > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("//a[contains(text(),'SEARCH SALES')]").click()
        driver.find_element_by_css_selector("#please-sign-in > footer > p > a").click()
        driver.find_element_by_name("first").clear()
        driver.find_element_by_name("first").send_keys("qa")
        driver.find_element_by_name("last").clear()
        driver.find_element_by_name("last").send_keys("test")
        driver.find_element_by_xpath("(//input[@name='email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("parola")
        driver.find_element_by_css_selector("#sign-up > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Neighborhoods").click()
        driver.find_element_by_link_text("CHELSEA").click()
        time.sleep(5)
        driver.find_element_by_link_text("BUY AN APARTMENT IN CHELSEA").click() # This link leads to the Rentals page instead of Sales (it happens just for Saucelabs test script file)
        time.sleep(5)
        driver.find_element_by_css_selector("#please-sign-in > footer > p > a").click() # It is not fount because it is not opening the Sales page but Rentals
        driver.find_element_by_name("first").clear()
        driver.find_element_by_name("first").send_keys("qa")
        driver.find_element_by_name("last").clear()
        driver.find_element_by_name("last").send_keys("test")
        driver.find_element_by_xpath("(//input[@name='email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("parola")
        driver.find_element_by_css_selector("#sign-up > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

