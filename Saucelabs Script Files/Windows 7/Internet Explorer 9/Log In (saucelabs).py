from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['version'] = '9'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Log In'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.set_window_size(1920,1200)
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
    
    def test_log_in(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='hamburger-navigation']/img").click()
        time.sleep(8)
        driver.find_element_by_xpath(".//*[@id='navigation']/ul/div/li[3]/a").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Sign up").click()
        driver.find_element_by_link_text("Log in!").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='hamburger-navigation']/img").click()
        time.sleep(8)
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(5)
        driver.find_element_by_link_text("SIGN UP FOR FREE").click()
        driver.find_element_by_link_text("Log in!").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='hamburger-navigation']/img").click()
        time.sleep(8)
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Rentals").click()
        time.sleep(5)
        driver.find_element_by_link_text("List").click()
        time.sleep(5)
        driver.find_element_by_link_text("SIGN UP FOR FREE").click()
        driver.find_element_by_link_text("Log in!").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='hamburger-navigation']/img").click()
        time.sleep(8)
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_xpath("//li[@id='save_search']/a/img").click()
        driver.find_element_by_css_selector("div.save_button").click()
        driver.find_element_by_link_text("Log in!").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(3)
        driver.find_element_by_id("hamburger-navigation").click()
        time.sleep(8)
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("hamburger-navigation").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Flatiron")
        driver.find_element_by_id("search_button").click()
        time.sleep(5)
        driver.find_element_by_id("listing-position-A").click()
        driver.find_element_by_link_text("CONTACT AGENT").click()
        driver.find_element_by_xpath(".//*[@id='contact-to-visit-anonymous']/footer/p/a").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='hamburger-navigation']/img").click()
        time.sleep(10)
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
