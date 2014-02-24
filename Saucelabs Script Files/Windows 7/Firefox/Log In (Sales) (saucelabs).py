from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '26'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Log In (Sales)'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_log_in_sales(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("i.ss-dropdown").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("//a[contains(text(),'SEARCH SALES')]").click()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Neighborhoods").click()
        driver.find_element_by_link_text("CHELSEA").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='experimental']/div[8]/div/a[1]").click()
        time.sleep(10)
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
