from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from random import random
from random import randint
import random as rn
my_string = 'string'

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        desired_capabilities['version'] = '7'
        desired_capabilities['platform'] = 'OS X 10.9'
        desired_capabilities['name'] = 'Favorite Button (Sales)'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com"
    
    def test_favorite_contact_to_visit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # Sign up with a new account
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sign up").click()
        driver.find_element_by_name("first").clear()
        driver.find_element_by_name("first").send_keys("qa")
        driver.find_element_by_name("last").clear()
        driver.find_element_by_name("last").send_keys("test")
        driver.find_element_by_xpath("(//input[@name='email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("parola")
        driver.find_element_by_css_selector("#sign-up > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("s2id_autogen1").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#select2-result-label-5").click()
        driver.find_element_by_xpath(".//*[@id='listing-position-A']/a").click()
        # Click on the Favorite button
        driver.find_element_by_css_selector(".ss-icon.ss-star").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("My Apartments").click()
        # See if the listing is set as a Favorite
        driver.find_element_by_link_text("Favorites").click()
        # Verifying if the listing is set as Favorite
        try:
            driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div/div[2]/div/div[3]/div/div/a")
            print "The listing is set as Favorite."
        except Exception ('ElementNotVisibleException'):
            print "The listing is not set as Favorite."
        # Submit the listing from the Favorite page
        driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/a/div[5]").click()
        # See if the listing is submitted
        driver.find_element_by_link_text("Request Status").click()
        # Verifying if the listing is submitted
        try:
            driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/a")
            print "The listing is submitted."
        except Exception ('ElementNotVisibleException'):
            print "The listing is not submitted."
        driver.find_element_by_css_selector("div.dropdown__link").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
