import unittest
from selenium import webdriver


class Testweb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/Users/Ranjitha/Downloads/geckodriver')
        self.driver.maximize_window()
        self.driver.get('http://www.demo.guru99.com/V4/')

    def test_search_by_name(self):
        user = self.driver.find_element_by_name('uid')
        user.send_keys('mngr227751')
        pw = self.driver.find_element_by_name('password')
        pw.send_keys('UjavEjE')
        login = self.driver.find_element_by_name('btnLogin')
        login.click()

        expected_res = "http://www.demo.guru99.com/V4/manager/Managerhomepage.php"
        actual_res = self.driver.current_url
        self.assertEqual(expected_res, actual_res, msg="Login Successful")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()







