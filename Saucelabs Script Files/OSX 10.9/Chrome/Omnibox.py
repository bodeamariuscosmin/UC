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
        desired_capabilities['platform'] = 'OS X 10.9'
        desired_capabilities['name'] = 'Omnibox'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(3)
        self.base_url = "https://staging.urbancompass.com"
    
    def test_ui(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        # Omnibox Zipcode for Sales
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("10003")
        zipcodeSale = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[2]/span/div[1]")
        print zipcodeSale.text
        if zipcodeSale.text == "Flatiron, Manhattan, 10003 - Sales":
            print "Zipcode for sale is found."
        else:
            print "Zipcode is NOT found."

        # Omnibox Zipcode for Rentals
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("10003")
        zipcodeRental = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[2]/span/div[2]")
        print zipcodeRental.text
        if zipcodeRental.text == "Flatiron, Manhattan, 10003 - Rentals":
            print "Zipcode for rental is found."
        else:
            print "Zipcode for rental is NOT found."

        # Omnibox Agent
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("Tak")
        agent = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[3]/span/div/div")
        print agent.text
        if agent.text == "Takk Yamaguchi":
            print "Agent found."
        else:
            print "Agent NOT found."

        # Omnibox Sale address
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("1 Jane St, Unit 1EXCLUSIVESALE")
        listingSale = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[5]/span/div")
        print listingSale.text
        if listingSale.text == "1 Jane St, Unit 1EXCLUSIVESALE - 1 bed / 1 bath / $1,000,000":
            print "Sale listing found."
        else:
            print "Sale listing NOT found."

        # Omnibox Rental address
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("1 Jane St, Unit 1EXCLUSIVERENTAL")
        listingRental = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[5]/span/div")
        print listingRental.text
        if listingRental.text == "1 Jane St, Unit 1EXCLUSIVERENTAL - 1 bed / 1 bath / $1,000":
            print "Rental listing found."
        else:
            print "Rental listing NOT found."

        # Omnibox Neighborhood sale
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("Chelsea")
        neighborhoodSale = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[1]/span/div[2]")
        print neighborhoodSale.text
        if neighborhoodSale.text == "Chelsea - Sales":
            print "Neighborhood Sale found."
        else:
            print "Neighborhood Sale NOT found."

        # Omnibox Neighborhood sale
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("Chelsea")
        neighborhoodRental = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[1]/span/div[1]")
        print neighborhoodRental.text
        if neighborhoodRental.text == "Chelsea - Rentals":
            print "Neighborhood Rental found."
        else:
            print "Neighborhood Rental NOT found."

        # Omnibox Neighborhood guide
        driver.find_element_by_name("smart_selector").clear()
        driver.find_element_by_name("smart_selector").send_keys("Chelsea")
        neighborhoodGuide = driver.find_element_by_xpath(".//*[@id='homepage-content']/div[1]/div/div[3]/div/span/span[2]/div[6]/span/div")
        print neighborhoodGuide.text
        if neighborhoodGuide.text == "Chelsea Neighborhood Guide":
            print "Neighborhood Guide found."
        else:
            print "Neighborhood Guide NOT found."
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
