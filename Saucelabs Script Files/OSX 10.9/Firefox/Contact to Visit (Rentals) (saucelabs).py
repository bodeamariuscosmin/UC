import unittest
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
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '26'
        desired_capabilities['platform'] = 'OS X 10.9'
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
        time.sleep(5)
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[3]").click()
        driver.find_element_by_css_selector(".listing-picker-popup>a").click()
        time.sleep(5)
        driver.find_element_by_css_selector(".btn.view").click()
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_name("phoneNumber").clear()
        driver.find_element_by_name("phoneNumber").send_keys("0000")
        driver.find_element_by_xpath("//input[@value='SUBMIT']").click()
        driver.find_element_by_xpath(".//*[@id='summary-form']/table/tbody[1]/tr/td[2]/div/label[1]").click()
        driver.find_element_by_css_selector("label").click()
        driver.find_element_by_name("roommates[relationship][]").clear()
        driver.find_element_by_name("roommates[relationship][]").send_keys("brother")
        driver.find_element_by_name("roommates[name][]").clear()
        driver.find_element_by_name("roommates[name][]").send_keys("Michael")
        driver.find_element_by_name("roommates[email][]").clear()
        driver.find_element_by_name("roommates[email][]").send_keys("michael@yahoo.com")
        driver.find_element_by_xpath(".//*[@id='summary-form']/table/tbody[4]/tr[1]/td[2]/div/label[1]").click()
        driver.find_element_by_xpath("//form[@id='summary-form']/table/tbody[4]/tr/td[2]/div/label").click()
        driver.find_element_by_name("breed").clear()
        driver.find_element_by_name("breed").send_keys("cat")
        driver.find_element_by_name("weight").clear()
        driver.find_element_by_name("weight").send_keys("1000")
        driver.find_element_by_xpath(".//*[@id='summary-form']/table/tbody[4]/tr[3]/td[2]/div/label[1]").click()
        driver.find_element_by_xpath("//form[@id='summary-form']/table/tbody[4]/tr[3]/td[2]/div/label").click()
        driver.find_element_by_name("customerNotes").clear()
        driver.find_element_by_name("customerNotes").send_keys("Notes.")
        driver.find_element_by_css_selector("input.button.button--primary").click()
        driver.find_element_by_link_text("Select Visit Times").click()
        driver.find_element_by_link_text("Edit Moving Info").click()
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[4]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[3]/div[2]/div/a[1]").click()
        time.sleep(5)
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        time.sleep(3)
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[3]/div[2]/div/a[1]").click()
        time.sleep(5)
        driver.find_element_by_css_selector(".btn.view").click()
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Brooklyn")
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_id("listing-position-A").click()
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Brooklyn")
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_id("listing-position-B").click()
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
