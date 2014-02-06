from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LogInSales(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.base_url = "https://staging.urbancompass.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_log_in_sales(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("i.ss-dropdown").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("//a[contains(text(),'SEARCH SALES')]").click()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Neighborhoods").click()
        driver.find_element_by_link_text("CHELSEA").click()
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='experimental']/div[8]/div/a[1]").click()
        time.sleep(10)
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").clear()
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > fieldset > input[name=\"email\"]").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath("(//input[@name='password'])[4]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("parola")
        driver.find_element_by_css_selector("#please-sign-in > div.modal_content > form > input[type=\"submit\"]").click()
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
