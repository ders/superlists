from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Arirang goes to the home page and accidentally tries to submit
        # an empty list item.  He then hits enter on the empty input box.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying that
        # list items cannot be blank.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # He tries again with some text for the item, and it now works.
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, he now decides to submit a second blank list item.
        self.get_item_input_box().send_keys('\n')

        # He receives a similar warning on the list page.
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And he can correct it by filling some list text in
        self.browser.get_item_imput_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
