from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        desired_capabilities['version'] = '7'
        desired_capabilities['platform'] = 'OS X 10.9'
        desired_capabilities['name'] = 'Change Password'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_change_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("My profile").click()
        driver.find_element_by_link_text("Change Password").click()
        driver.find_element_by_xpath(".//*[@id='update-password-form']/table/tbody/tr[1]/td[2]/input").send_keys("parola")
        driver.find_element_by_xpath(".//*[@id='update-password-form']/table/tbody/tr[2]/td[2]/input").send_keys("a")
        driver.find_element_by_xpath(".//*[@id='update-password-form']/table/tbody/tr[3]/td[2]/input").send_keys("a")
        driver.find_element_by_id("update-password").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("a")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("My profile").click()
        driver.find_element_by_link_text("Change Password").click()
        driver.find_element_by_name("currentPassword").clear()
        driver.find_element_by_name("currentPassword").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("parola")
        driver.find_element_by_name("passwordConfirmation").clear()
        driver.find_element_by_name("passwordConfirmation").send_keys("parola")
        driver.find_element_by_id("update-password").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
