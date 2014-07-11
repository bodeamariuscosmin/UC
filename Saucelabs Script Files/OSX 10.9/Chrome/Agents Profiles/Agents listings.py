from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '28'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Agents listings'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(5)
        self.base_url = "https://staging.urbancompass.com/agents/profiles/view/jennifer_baker"
    
    def test_ui(self):
        driver = self.driver
        driver.get(self.base_url + "")

        inputElement = driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[3]")
        print inputElement.text

        inputElement = driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[4]")
        print inputElement.text

    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
