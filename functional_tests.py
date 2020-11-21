"""File: functional_tests_py
https://www.obeythetestinggoat.com/book/chapter_01.html
https://www.guru99.com/selenium-python.html

Remember! First set up dev server with command in 
the directory of this file (Django project root):
$ python manage.py runserver

Then run this script (as a script, still in root) with command:
$ python functional_tests.py

Alternatively, run as a module, (exactly?) the same outcome:
$ python -m functional_tests
Note: "-m" but no ".py"
""" 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#cap = DesiredCapabilities().FIREFOX
#cap["marionette"] = False

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
class SelectAndDisplayStudentTest(unittest.TestCase):  
    """Goat book example
    https://www.obeythetestinggoat.com/book/chapter_02_unittest.html
    """
    def setUp(self):  
        # browser = driver.Firefox(desired_capabilities=capabilities)
        #browser = webdriver.Firefox(firefox_binary='/home/morten/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary='/home/morten/firefox/firefox')
        #browser = webdriver.Firefox(firefox_binary='/home/morten/firefox/firefox-bin')
        self.browser.get('http://localhost:8000')


    def tearDown(self):  
        self.browser.quit()
    
    def test_landing_page_title(self):
        """ Edith goes to landing page of boxplot app.
        """
        # She reads the title in browser tab
        self.assertEqual('Demo boxplot', self.browser.title)  

    def test_landing_page_has_link_home(self):  
        """ Edith goes to landing page of boxplot app, finds link to same page.
        """
#        self.browser.get('http://localhost:8000')

        # in the footer, a link back to the index is displayed
        # Deprecated: assertDictContainsSubset() <- https://github.com/pylover/restfulpy/issues/186
        # https://selenium-python.readthedocs.io/locating-elements.html
        # 
        ### TypeError: argument of type 'FirefoxWebElement' is not iterable
        home_link = self.browser.find_element_by_link_text('Demo startside')
        ### Type: https://www.selenium.dev/documentation/en/webdriver/web_element/
        ### NB: landing_page_link.get_attribute('href') gives ABSOLUTE URL
        ### 'http://localhost:8000/', NOT the RELATIVE string '/' entered in template HTML!
        self.assertEqual( 
            home_link.get_attribute('href'),
            'http://localhost:8000/'
        )
        #self.fail(f'Fails, because it is asked to. Reminds you: "Finish writing the test!"')  
        
    def test_landing_page_has_link_to_github(self):  
        """ Edith goes to landing page of boxplot app, finds link to GitHub repo.
        """
        # in the footer, a link to Github/engelsmann/boxplot is displayed
        github_link = self.browser.find_element_by_link_text('GitHub repo')

        self.assertEqual( 
            github_link.get_attribute('href'),
            'https://github.com/engelsmann/boxplot'
        )

    def test_student_name_to_left_of_radio_button(self, student_name = 'Helle Byskov', student_id=7):  
        """To the left of the selected student name, the radio button for this person appears
        """
        student_radio_id = f'elev{student_id}' # Duplicate to test that label is name
        student_label_list = self.browser.find_elements(By.TAG_NAME, 'label')
        label_for_radios = [el.get_attribute("for") for el in student_label_list]
#        student_radio = self.browser.find_element(By.ID, student_radio_id)
        self.assertIn(
            student_radio_id,
            label_for_radios
        )
    def test_can_select_a_student(self, student_name = 'Helle Byskov', student_id=7):  
        """You click on a student's name
        https://www.guru99.com/checkbox-and-radio-button-webdriver.html
        """
        student_radio_id = f'elev{student_id}' # Duplicate to test that label is name
#        student_radio = self.browser.find_element_by_id(student_radio_id)
        student_radio = self.browser.find_element_by_css_selector(
            f"input[type='radio'][value='{student_radio_id}']"
            )
        student_radio.click()
        self.assertTrue(
            student_radio.is_selected(),
        )

        

        # The radio button is selected

        # You press the SUBMIT button

        # You are send to the display page, "/"

        # This page has the selected student's name in its title

        # Page H2 headline tells the assignment title

        # A chart is displayed

        # in the footer, a link back to the index is displayed

        # in the footer, a link to Github/engelsmann/boxplot is displayed


if __name__ == '__main__':  
    unittest.main()
