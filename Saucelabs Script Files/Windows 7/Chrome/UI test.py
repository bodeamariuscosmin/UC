from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = '31'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'UI test'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_change_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
            driver.find_element_by_id("logo")
            print "The UC logo is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[2]")
            print "The homepage content is present!"
        except Exception ('ElementNotVisibleException'):
            print "The homepage content is missing."

        try:
            driver.find_element_by_xpath(".//*[@id='homepage-content']/div[2]/div[4]")
            print "The carousel is present!"
        except Exception ('ElementNotVisibleException'):
            print "The carousel is missing."

        try:
            driver.find_element_by_link_text("Rentals")
            print "The Rentals button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Rentals button is missing."

        try:
            driver.find_element_by_link_text("Sales")
            print "The Sales button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Sales button is missing."

        try:
            driver.find_element_by_link_text("Agents")
            print "The Agents button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Agents button is missing."

        try:
            driver.find_element_by_link_text("My Apartments")
            print "The My Apartments button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The My Apartments button is missing."

        try:
            driver.find_element_by_link_text("Neighborhoods")
            print "The Neighborhoods button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Neighborhoods button is missing."

        try:
            driver.find_element_by_link_text("Log in")
            print "The Log In button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Log In button is missing."

        try:
            driver.find_element_by_link_text("Sign up")
            print "The Sign Up button is present!"
        except Exception ('ElementNotVisibleException'):
            print "The Sign Up button is missing."

        try:
            driver.find_element_by_id("press")
            print "The press is present!"
        except Exception ('ElementNotVisibleException'):
            print "The press button is missing."
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
