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
        desired_capabilities['name'] = 'Contact to Visit (Sales)'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_sales_contact_to_visit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
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
        driver.find_element_by_link_text("CONTACT AGENT").click()
        driver.find_element_by_xpath("html/body/div[3]/section[21]/div[2]/form/div[1]/input").clear()
        driver.find_element_by_xpath("html/body/div[3]/section[21]/div[2]/form/div[1]/input").send_keys("0000")
        driver.find_element_by_xpath("html/body/div[3]/section[21]/div[2]/form/input").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sales").click()
        '''driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("s2id_autogen1").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#select2-result-label-5").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='listing-position-B']/a").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Contact Agent')])[2]").click()
        driver.find_element_by_xpath(".//*[@id='allocation-random-agent']/div[2]/form/input").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sales").click() '''
        driver.find_element_by_link_text("Map").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sales").click() # Avoiding the returning from List view to Map view bug 
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[4]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[3]/div[2]/div/a[1]").click()
        time.sleep(1)
        driver.find_element_by_link_text("CONTACT AGENT").click()
        driver.find_element_by_xpath("html/body/div[3]/section[21]/div[2]/form/input").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
