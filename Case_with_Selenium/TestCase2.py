# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


import logging
LOGGER = logging.getLogger(__name__)

class TestCase2:
    def setup_method(self, method):
        self.driver = webdriver.Chrome("../chromedriver/chromedriver")



    def teardown_method(self, method):

        pass

    def test_case2(self):
        self.driver.get("https://blog.griddynamics.com/")
        self.driver.set_window_size(1440, 790)


        element = self.driver.find_element(By.LINK_TEXT, "Insights")
        assert element.is_displayed()
        element.click()


        # element = self.driver.find_element(By.XPATH, "//div[@id='topiclist']")
        #element = self.driver.find_element(By.XPATH, "//div[@id='topiclist']//div//span[@class='selected'][normalize-space()='All topics']")
        #element.click()
        #assert element.is_displayed()

        #element.send_keys('Cloud and DevOps')
        # cloud devops in filter
        # element = self.driver.find_element(By.XPATH, "//div[@id='topiclist']//div//span[@class='selected'][normalize-space()='All topics']")
        # element.click()
        # assert element.is_displayed()



        # cloud devops in filter
        element= self.driver.find_element(By.XPATH, "//div[@id='topiclist']//div//span[@class='selected']")

        self.driver.execute_script("arguments[0].innerText='Cloud and DevOps'", element)
        # element_cloud = self.driver.find_element(By.XPATH, "//span[@data-value='cloud-and-devops']")
        # self.driver.execute_script("arguments[0].setAttribute('class',arguments[1])", element_cloud, 'selected')
        LOGGER.critical(f"List:{element}")
        element.click()
        assert element.is_displayed()

        # element.send_keys('Cloud and DevOps')

        #element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-5 > .ng-star-inserted:nth-child(1) span")
        #assert element.is_displayed()
        #element.click()

        #element5 = self.driver.find_elements(By.XPATH, "//A[@_ngcontent-gd-website-c71='']")
        #LOGGER.critical(f"List:{len(element5)}")
        #assert len(element5) > 0

