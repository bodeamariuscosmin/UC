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
        desired_capabilities['name'] = 'UI test'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://mariusb:bd27d6b0-f987-4773-b20b-633da38327de@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.urbancompass.com/agents/profiles"
    
    def test_agents_profiles(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
            driver.find_element_by_link_text("Jasmin Aydagul")
            print "Jasmin Aydagul is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Jennifer Baker")
            print "Jennifer Baker is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Rafael Barbosa")
            print "Rafael Barbosa is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Matt Baren")
            print "Matt Baren is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Tom Baron")
            print "Tom Baron is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Robert Bell")
            print "Robert Bell is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Jared Belson")
            print "Jaren Belson is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Ross Brown")
            print "Ross Brown is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Sandu Calinescu")
            print "Sandu Calinescu is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Alberto Cordoba")
            print "Alberto Cordoba is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Natalia Correa")
            print "Natalia Correa is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Justin Croushore")
            print "Justin Croushore is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Blake Eisenberg")
            print "Blake Eisenberg is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Udi Eliasi")
            print "Udi Eliasi is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Christopher Fusco")
            print "Christopher Fusco is present!"
        except Exception ('ElementNotVisibleException'):
            print "The UC logo is missing."

        try:
            driver.find_element_by_link_text("Josh Galdos")
            print "Josh Galdos is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Yaal Gluska")
            print "Yaal Gluska is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Mark Griffith")
            print "Mark Griffith is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        '''try:
            driver.find_element_by_link_text("Elicia Guarino")
            print "Elicia Guarino is present!"
        except Exception ('ElementNotVisibleException'):
            print ""'''

        try:
            driver.find_element_by_link_text("Zach Gutierrez")
            print "Zach Gutierrez is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Mike Halpern")
            print "Mike Halpern is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Kristin Herrera")
            print "Kristin Herrera is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("John Huston")
            print "John Huston is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Michael King")
            print "Michael King is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Ian Lane")
            print "Ian Lane is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Claudia Lesnaya")
            print "Claudia Lesnaya is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Stephen Litman")
            print "Stephen Litman is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Alex Livshiz")
            print "Alex Lishviz is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Christine Mariani")
            print "Christine Mariani is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Richard Miglio")
            print "Richard Miglio is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Sean Mottola")
            print "Sean Mottola is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Tim Perkins")
            print "Tim Perkins is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Andrew Plichta")
            print "Andrew Plichta is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Ryan Ragone")
            print "Ryan Ragone is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Angel Ramirez")
            print "Angel Ramirez is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Christopher Ritchey")
            print "Christopher Ritchey is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Jason Saft")
            print "Jason Saft is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Tom Salzano")
            print "Tom Salzano is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Cindy Scholz")
            print "Cindy Scholz is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Deirdre Scott")
            print "Deirdre Scott is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Corinne Smith")
            print "Corinne Smith is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Sandra Smith")
            print "Sandra Smith is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Scott Sobol")
            print "Scott Sobol is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Carlota Sosa")
            print "Carlota Sosa is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Cameron Stewart")
            print "Cameron Stewart is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Katie Thurber")
            print "Katie Thurber is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Jake Velazquez")
            print "Jake Velazquez is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Michael Walter")
            print "Michael Walter is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Tony Wilson")
            print "Tony Wilson is present!"
        except Exception ('ElementNotVisibleException'):
            print ""

        try:
            driver.find_element_by_link_text("Takk Yamaguchi")
            print "Takk Yamaguchi is present!"
        except Exception ('ElementNotVisibleException'):
            print ""
        


    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
