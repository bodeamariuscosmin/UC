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
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = '31'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Contact to Visit (Rentals)'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_contact_to_visit_rentals(self):
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
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("Map").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[3]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[2]").click()
        driver.find_element_by_css_selector(".listing-picker-popup>a").click()
        time.sleep(5)
        # Submitting a listing from the map modal
        driver.find_element_by_link_text("CONTACT AGENT").click()
        # Agent allocation
        driver.find_element_by_xpath(".//*[@id='allocation-phone-number']").clear()
        driver.find_element_by_xpath(".//*[@id='allocation-phone-number']").send_keys("0000")
        driver.find_element_by_id("allocation-optional-message").clear()
        driver.find_element_by_id("allocation-optional-message").send_keys("Quality Assurance test")
        driver.find_element_by_xpath(".//*[@id='allocation-random-agent']/div[2]/form/input").click()

        driver.find_element_by_link_text("MY APARTMENTS").click()
        
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Chinatown")
        driver.find_element_by_id("search_button").click()
        # Submitting a listing from the first Contact Agent button
        driver.find_element_by_id("listing-position-A").click()
        driver.find_element_by_link_text("CONTACT AGENT").click()
        # Agent allocation
        # driver.find_element_by_id("allocation-optional-message").clear()
        driver.find_element_by_id("allocation-optional-message").send_keys("Quality Assurance test")
        # driver.find_element_by_xpath(".//*[@id='allocation-agent']/div[2]/form/input").click()
        # driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_xpath(".//*[@id='allocation-random-agent']/div[2]/form/input").click()
        driver.find_element_by_link_text("MY APARTMENTS").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Chinatown")
        driver.find_element_by_id("search_button").click()
        # Submitting a listing from the second Contact Agent button
        driver.find_element_by_id("listing-position-B").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Contact Agent')])[2]").click()
        # Agent allocation
        driver.find_element_by_xpath(".//*[@id='allocation-random-agent']/div[2]/form/input").click()
        driver.find_element_by_link_text("MY APARTMENTS").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
