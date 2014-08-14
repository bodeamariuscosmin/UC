import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '30'
        desired_capabilities['platform'] = 'OS X 10.9'
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
        driver.find_element_by_id("hamburger-navigation").click()
        # Log in from the rental map/list modal
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[1]/input").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/input").click()
        time.sleep(2)
        driver.find_element_by_id("hamburger-navigation").click()
        time.sleep(1)
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
