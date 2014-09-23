import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from random import random
from random import randint
import random as rn
my_string = 'string'


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        desired_capabilities['version'] = '7'
        desired_capabilities['platform'] = 'OS X 10.9'
        desired_capabilities['name'] = 'Sign Up'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"

    def test_sign_up(self): # Bug: Logged users not always log out and this makes the test to fail. 
        driver = self.driver
        driver.get(self.base_url + "/")
        # Sign up from the header
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
        time.sleep(3)
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()

        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("s2id_autogen1").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#select2-result-label-5").click()
        driver.find_element_by_xpath(".//*[@id='listing-position-A']/a").click()
        # Sign up from Contact to visit
        driver.find_element_by_link_text("CONTACT AGENT").click()
        time.sleep(2)
        driver.find_element_by_css_selector("div.input-2 > input[name=\"first\"]").clear()
        driver.find_element_by_css_selector("div.input-2 > input[name=\"first\"]").send_keys("qa")
        driver.find_element_by_css_selector("div.input-2 > input[name=\"last\"]").clear()
        driver.find_element_by_css_selector("div.input-2 > input[name=\"last\"]").send_keys("test")
        driver.find_element_by_css_selector("#contact-to-visit-anonymous > div:nth-child(3) > form:nth-child(2) > fieldset:nth-child(2) > input:nth-child(2)").clear()
        driver.find_element_by_css_selector("#contact-to-visit-anonymous > div:nth-child(3) > form:nth-child(2) > fieldset:nth-child(2) > input:nth-child(2)").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[5]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[5]").send_keys("parola")
        driver.find_element_by_xpath(".//*[@id='contact-to-visit-anonymous']/div[2]/form/fieldset[4]/input").click()
        driver.find_element_by_xpath(".//*[@id='contact-to-visit-anonymous']/div[2]/form/fieldset[4]/input").send_keys("0000")
        driver.find_element_by_xpath(".//*[@id='contact-to-visit-anonymous']/div[2]/form/input").click()
        driver.find_element_by_xpath("//input[@value='Create an account to visit']").click()
        # Agent allocation
        driver.find_element_by_xpath("html/body/div[3]/section[21]/div[2]/form/input").click()
        driver.find_element_by_link_text("MY APARTMENTS").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        # Sign up from Email Alert

        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_xpath("//li[@id='save_search']/a/img").click()
        driver.find_element_by_css_selector("div.save_button").click()
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
        driver.find_element_by_id("notify-immediately").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()


    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
