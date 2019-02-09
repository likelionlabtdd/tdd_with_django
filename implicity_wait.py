from selenium import webdriver
import unittest

class SaveTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(10) # 10초만큼
        self.browser.get('http://www.naver.com')

    def test_StartWebPage_AndLater(self):
        aa = self.browser.find_element_by_css_selector('div.isnotpossible')                                                                                                                                                                                                     
        self.assertIn('To-Do', aa)
    

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

                                                                                                                                                                                                                              
