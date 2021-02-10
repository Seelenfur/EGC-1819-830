import time

from authentication.models import UserProfile
from base import mods
from base.tests import BaseTestCase
from django.contrib import auth
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class AppDynamicsJob(StaticLiveServerTestCase):
  def setUp(self):
      self.base = BaseTestCase()
      self.base.setUp()

      options = webdriver.ChromeOptions()
      options.headless = True
      self.driver = webdriver.Chrome(options=options)

      super().setUp()

  def tearDown(self):
      super().tearDown()
      self.driver.quit()

      self.base.tearDown()           
            
  
  def test_pruebabien(self):
    driver = self.driver
    self.get(f'{self.live_server_url}/')
    self.driver.set_window_size(550, 691)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#content > h1").click()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()
