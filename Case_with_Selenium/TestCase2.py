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


class TestCase2:
    def setup_method(self, method):
        self.driver = webdriver.Chrome("/Users/afisher/Downloads/chrome_drivers/98/chromedriver")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_case2(self):
        self.driver.get("https://blog.griddynamics.com/")
        self.driver.set_window_size(1440, 790)
        element = self.driver.find_element(By.LINK_TEXT, "Solutions")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Solutions").click()

        element = self.driver.find_element(By.CLASS_NAME, "solutions-filter__facets")
        assert element.is_displayed()

        element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-5 > .ng-star-inserted:nth-child(1) span")
        assert element.is_displayed()
        element.click()
        #
        self.driver.find_element(By.XPATH, "//a[@class='card-block ng-star-inserted']").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,218.5)")
        self.driver.execute_script("window.scrollTo(0,216)")
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-18 > .ng-star-inserted:nth-child(1) > label").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .description-label").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,242)")
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,251.5)")
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) > label").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) > label").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-27 > .ng-star-inserted:nth-child(1) span").click()
