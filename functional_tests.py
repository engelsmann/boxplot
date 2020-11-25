"""File: functional_tests.py
https://www.obeythetestinggoat.com/book/chapter_01.html
https://www.guru99.com/selenium-python.html
https://docs.djangoproject.com/en/3.1/intro/tutorial05/#tests-don-t-just-identify-problems-they-prevent-them
Test order: https://stackoverflow.com/q/4095319/888033
Remember! In order to run this suite of tests, you must 
first set up dev server in the directory of this file 
(Django project root) with command :

$ python manage.py runserver

Then run this script (as a script, still in root) with command:

$ python functional_tests.py

Alternatively, run as a module, (exactly?) the same outcome:

$ python -m functional_tests

Note: "-m" but no ".py"
"""
# Simulated web browser user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium                                       import webdriver
from selenium.webdriver.common.by                   import By
from selenium.webdriver.common.keys                 import Keys
### https://selenium-python.readthedocs.io/api.html#selenium.webdriver.support.wait.WebDriverWait
from selenium.webdriver.support.ui                  import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
# Test runner (deploying the WebDriver)
import unittest
class SelectStudentTest(unittest.TestCase):
    """Goat book example
    https://www.obeythetestinggoat.com/book/chapter_02_unittest.html
    ResourceWarning: https://github.com/deepmind/pysc2/issues/243
    - The warning is a warning, no error. Keep calm and carry on.
    - Appears in conjunction with a "timeout.py". Could it be that the web driver is too slow,
    e.g. to close down window??
    """

    def setUp(self, student_id=7):
        self.browser = webdriver.Firefox(
            firefox_binary='/home/morten/firefox/firefox')
        self.browser.get('http://localhost:8000')
        self.wait = WebDriverWait(self.browser, 20)
        # Find INPUT field of type 'radio' in FORM.
        # The field must have ID  == student_id.
        # selenium.webdriver.common.by.By
        # https://selenium-python.readthedocs.io/api.html#locate-elements-by
        first_button = self.browser.find_element( 
            By.CSS_SELECTOR,
            f'input[type="radio"][id="elev{student_id}"]' 
            )
        first_button.click()

    def tearDown(self):
        self.browser.quit()

    def test_landing_page(self):
        """ Edith goes to landing page of boxplot app.
        """
        # She reads the title in browser tab
        self.assertEqual('Demo boxplot', self.browser.title)

    def test_landing_page_has_home_links(self):
        """ Edith goes to landing page of boxplot app, finds link to same page.
        """
        self.browser.get('http://localhost:8000')

        # in the footer, a link back to the index is displayed
        # Deprecated: assertDictContainsSubset() <- https://github.com/pylover/restfulpy/issues/186
        # https://selenium-python.readthedocs.io/locating-elements.html
        #
        # TypeError: argument of type 'FirefoxWebElement' is not iterable
        home_link = self.browser.find_element_by_link_text('Demo startside')
        # Type: https://www.selenium.dev/documentation/en/webdriver/web_element/
        # NB: landing_page_link.get_attribute('href') gives ABSOLUTE URL
        # 'http://localhost:8000/', NOT the RELATIVE string '/' entered in template HTML!
        self.assertEqual(
            home_link.get_attribute('href'),
            'http://localhost:8000/'
        )

    def landing_page_has_github_link(self):
        """ Edith goes to landing page of boxplot app, finds link to GitHub repo.
        """
        # in the footer, a link to Github/engelsmann/boxplot is displayed
        # self.browser.get('http://localhost:8000')
        github_link = self.browser.find_element_by_link_text('GitHub repo')

        self.assertEqual(
            github_link.get_attribute('href'),
            'https://github.com/engelsmann/boxplot'
        )

    def test_can_select_a_student(self, student_name='Helle Byskov', student_id=7):
        """You click on a student's name -> The correct radio button is selected
        https://www.guru99.com/accessing-forms-in-webdriver.html
        https://www.guru99.com/checkbox-and-radio-button-webdriver.html
        """
        student_radio = self.browser.find_element_by_css_selector(
            f"input[type='radio'][id='elev{student_id}']"
        )
        student_radio.click()
        self.assertTrue(
            student_radio.is_selected()
        )
        
    # Selecting a student who has not received assesment is handled
    # Selecting a student who has not received assesment (KeyError) results in meaningful message

    def test_keyerror_on_student_not_assessed(self, student_name='Andersine Andersen', student_id=1):
        """Page not reached if student selected did not receive assessment
        """
        self.browser = webdriver.Firefox(
            firefox_binary='/home/morten/firefox/firefox')
        self.browser.get("http://127.1:8000")
        student_radio_button = self.wait.until(
            presence_of_element_located(
                (By.CSS_SELECTOR,
                 f'input[type="radio"][id="elev{student_id}"]')
            )
        )
        student_radio_button.click()

        form_submit = self.browser.find_element_by_css_selector(
            "input[type='submit']"
            )
        form_submit.click()
        self.assertGreater(
            self.browser.title.find("KeyError"),
            -1,
            "Proceeding to chart page with "+student_name+" did not raise KeyError as expected."
            )
        # Tried, unsuccesful ...
        # https://stackoverflow.com/a/6103983/888033
        #with self.assertRaises(KeyError):
        #    form_submit.click()
        # AssertionError: KeyError not raised

        

    def test_h2_after_submitted(self, student_name='Helle Byskov', student_id=7, assignment_title="covid"):
        # Page after submit shows H2 headline tellling the assignment title
        self.browser.get("http://127.1:8000")
        
        student_radio = self.browser.find_element_by_css_selector(
            f"input[type='radio'][id='elev{student_id}']"
        )
        student_radio.click()

        form_submit = self.browser.find_element_by_css_selector(
            "input[type='submit']"
            )
        form_submit.click()

        page_title = self.browser.find_element_by_tag_name(
            "h2"
            ).get_attribute("innerHTML")
        self.assertGreater(
            page_title.find(assignment_title),
            -1,
            f"Assignment '{assignment_title}'' not found in H2 headline."
        )

    def test_img_after_submitted(self, student_name='Helle Byskov', student_id=7):
        # E: timeout
        # A chart is displayed, that is: A HTML tag named "img" is present.
        self.browser = webdriver.Firefox(
            firefox_binary='/home/morten/firefox/firefox'
            )
        self.browser.get("http://127.1:8000")
        student_radio = self.browser.find_element_by_css_selector(
            f"input[type='radio'][id='elev{student_id}']"
        )
        student_radio.click()

        form_submit = self.browser.find_element_by_css_selector(
            "input[type='submit']"
            )
        form_submit.click()

        # The image embedded as string
        img_element = self.browser.find_element_by_tag_name("img")
        src = img_element.get_attribute('src')
        # The expected beginning of that string
        needle = 'image/png;'
        self.assertGreater(
            src.find(needle),
            -1, # Not found
            "Image string should start with code including 'image/png'."
        )

        # In the footer, a link back to the index is displayed

        # In the footer, a link to Github/engelsmann/boxplot is displayed
        #self.fail(f'Fails, because it is asked to. Reminds you: "Finish writing the test!"')


if __name__ == '__main__':
    ### The unittest test runner, which will automatically find test classes and methods in the file and run them.
    unittest.main()
