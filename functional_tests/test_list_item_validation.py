from .base import FunctionalTest
from lists.forms import EMPTY_LIST_ERROR, DUPLICATE_ITEM_ERROR

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Arirang goes to the home page and accidentally tries to submit
        # an empty list item.  He then hits enter on the empty input box.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying that
        # list items cannot be blank.
        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        # He tries again with some text for the item, and it now works.
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, he now decides to submit a second blank list item.
        self.get_item_input_box().send_keys('\n')

        # He receives a similar warning on the list page.
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        # And he can correct it by filling some list text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Arirang goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # He accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # He sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)

    def test_error_messages_are_cleared_on_input(self):
        # Arirang starts a new list in a way that causes a validation error.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # He starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # He is pleased to see that the error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
