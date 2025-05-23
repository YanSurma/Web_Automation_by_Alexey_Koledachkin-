from tests.base_test import BaseTest


class TestRegistrationPage(BaseTest):

    def test_create_account(self):
        self.registration_page.open()
        self.registration_page.fill_first_name()
        self.registration_page.fill_last_name()
        self.registration_page.fill_email()
        self.registration_page.fill_re_email()
        self.registration_page.fill_username()
        self.registration_page.fill_password()
        self.registration_page.fill_birthday()
        self.registration_page.click_to_male_radiobutton()
        self.registration_page.click_to_privacy_policy_checkbox()
        self.registration_page.click_create_account_button()
        self.registration_page.check_success_text_after_registration()
