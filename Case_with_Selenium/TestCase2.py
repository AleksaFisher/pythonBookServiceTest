# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import logging
LOGGER = logging.getLogger(__name__)

class TestCase2:
    def setup_method(self, method):
        self.driver = webdriver.Chrome("/Users/afisher/Downloads/chrome_drivers/98/chromedriver")

    # self.vars = {}

    def teardown_method(self, method):
        # self.driver.quit()
        pass

    def test_case2(self):
        self.driver.get("https://blog.griddynamics.com/")
        self.driver.set_window_size(1440, 790)


        element = self.driver.find_element(By.LINK_TEXT, "Solutions")
        assert element.is_displayed()
        element.click()

        # element = self.driver.find_element(By.XPATH,
        #                                    "(//*[contains(_ngcontent-gd-website-c68,'')][contains(text(),'Filter by')])")
        element = self.driver.find_element(By.CLASS_NAME, "solutions-filter__facets")
        assert element.is_displayed()
        # cloud devops in filter



        element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-5 > .ng-star-inserted:nth-child(1) span")
        assert element.is_displayed()
        element.click()

        element5 = self.driver.find_elements(By.XPATH, "//A[@_ngcontent-gd-website-c71='']")

        # < a
        # _ngcontent - gd - website - c71 = ""
        # cdkmonitorelementfocus = ""
        #
        # class ="card-block ng-star-inserted" href="/solutions/analytical-data-platform" > < div _ngcontent-gd-website-c71="" class ="gd-typography-h4 title-label" > Analytics platform < / div > < div _ngcontent-gd-website-c71="" class ="divider ng-star-inserted" > < / div > < !----> < div _ngcontent-gd-website-c71="" class ="description-label ng-star-inserted" > Increase speed to insights.Manage enterprise data assets, migrate from on-premise EDW to cloud, improve data accessibility & amp; quality, & amp; increase ROI.< / div > < !----> < gd-icon _ngcontent-gd-website-c71="" name="arrow-right" class ="read-more-icon ui-icon-standard-layout" aria-hidden="true" role="img" data-ui-icon-key="/assets/icons/arrow-right.svg" > < svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" > < path d="M12.7 4.4a1 1 0 10-1.4 1.4zm6.3 7.7l.7.7c.4-.4.4-1 0-1.4zm-7.7 6.3a1 1 0 001.4 1.4zm0-12.6l7 7 1.4-1.4-7-7zm7 5.6l-7 7 1.4 1.4 7-7z" > < / path > < path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M19 12.1H5" > < / path > < / svg >
        #
        # < / gd - icon > < / a >

        LOGGER.critical(f"List:{len(element5)}")
        assert len(element5) > 0
#         #
#
#         #
#         # self.driver.find_element(By.XPATH, "//a[@class='card-block ng-star-inserted']").click()
#
# #
#         element = self.driver.find_element(By.XPATH, "//A[@_ngcontent-gd-website-c71='']")
#         element.is_displayed()
#
#         self.driver.execute_script("window.scrollTo(0,0)")
#         self.driver.execute_script("window.scrollTo(0,218.5)")
#         self.driver.execute_script("window.scrollTo(0,216)")
#         # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-18 > .ng-star-inserted:nth-child(1) > label").click()
#         # self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .description-label").click()
#         self.driver.execute_script("window.scrollTo(0,0)")
#         self.driver.execute_script("window.scrollTo(0,242)")
#         self.driver.execute_script("window.scrollTo(0,0)")
#         self.driver.execute_script("window.scrollTo(0,251.5)")
#         # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) > label").click()
#         # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) > label").click()
#         # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) span").click()
#         # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) span").click()
