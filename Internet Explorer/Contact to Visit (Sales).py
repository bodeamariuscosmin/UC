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

class SalesContactToVisit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging.urbancompass.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sales_contact_to_visit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_link_text("Sign up").click()
        driver.find_element_by_name("first").clear()
        driver.find_element_by_name("first").send_keys("qa")
        driver.find_element_by_name("last").clear()
        driver.find_element_by_name("last").send_keys("test")
        driver.find_element_by_xpath("(//input[@name='email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("qa+"+str(rn.randint(0,99999))+"@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-up']/div[2]/form/fieldset[4]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-up > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(5)
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Brooklyn")
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_id("listing-position-A").click()
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_name("phoneNumber").clear()
        driver.find_element_by_name("phoneNumber").send_keys("0000")
        driver.find_element_by_xpath("//input[@value='SUBMIT']").click()
        driver.find_element_by_id("modal_overlay").click()
        time.sleep(5)
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Brooklyn")
        driver.find_element_by_id("search_button").click()
        time.sleep(5)
        driver.find_element_by_id("listing-position-B").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Contact to Visit')])[2]").click()
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Sales").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[3]").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='map']/div/div[1]/div/div[2]/div[2]/div[3]").click()
        time.sleep(5)
        driver.find_element_by_css_selector(".listing-picker-popup>a").click()
        time.sleep(5)
        driver.find_element_by_link_text("CONTACT TO VISIT").click()
        driver.find_element_by_link_text("CONTINUE SEARCHING").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
