from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Arirang has heard about a cool new online to-do app.  He goes to
        # check out its homepage.
        self.browser.get(self.server_url)

        # He notices the page title and header mention to-do lists.
        self.assertIn('To-do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

        # He is invited to enter a to-do item straight away.
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feathers" into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)
        arirang_list_url = self.browser.current_url
        self.assertRegex(arirang_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting him to add another item.
        # He enteres "Use peacock feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again and now shows both items on his list.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Now a new user, Seurirang, comes along to the site.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Seurirang visits the home page.  There is no sign of Arirang's list.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Seurirang starts a new list by entering a new item.  Hi is less
        # interesting than Arirang.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Seurirang gets his own unique URL.
        seurirang_list_url = self.browser.current_url
        self.assertRegex(seurirang_list_url, '/lists/.+')
        self.assertNotEqual(seurirang_list_url, arirang_list_url)

        # Again, there is no trace of Arirang's list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, Arirang goes back to sleep.
