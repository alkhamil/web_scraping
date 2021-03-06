import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
import unittest
import time
import datetime
import os

import scrool


class Test(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1366x768")
        chrome_driver = '/var/www/html/capture_web/driver/chromedriver'
        self.driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=chrome_driver)

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        print("Prosessing start ...")
        paths = [
            {"app": "IPR", "dir": "/var/www/html/hasil_web/ipr/",
             "site": [
                 {"link": "http://imaniprima.co.id", "ket": "HOME"},
                 {"link": "http://imaniprima.co.id/CONTACT-us/",
                  "ket": "CONTACT"}
             ]
             }]
        tgl = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        for path in paths:
            if not os.path.exists(path['dir']):
                os.makedirs(path['dir'])
            for site in path['site']:
                try:
                    self.driver.get(site['link'])
                    time.sleep(5)
                    scrool.fullpage_screenshot(
                        self.driver, path['dir'] + '/' + path['app'] + "_" + site['ket'] + "_" + tgl + '.png')
                except:
                    print("Error prosessing" + site['link'])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
