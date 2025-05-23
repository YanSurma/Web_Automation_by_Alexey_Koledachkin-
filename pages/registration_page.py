from faker import Faker
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/'
    _FIRST_NAME_INPUT = '//input[@name="firstname"]'
    _LAST_NAME_INPUT = '//input[@name="lastname"]'
    _EMAIL_INPUT = '//input[@name="email"]'
    _RE_EMAIL_INPUT = '//input[@name="email_re"]'
    _USERNAME_INPUT = '//input[@name="username"]'
    _PASSWORD_INPUT = '//input[@name="password"]'
    _BIRTHDAY_INPUT = '//input[@name="birthdate"]'
    _MONTH_PICKER = '//select[@class="ui-datepicker-month"]'
    _YEAR_PICKER = '//select[@class="ui-datepicker-year"]'
    _DAY_PICKER = '//a[@data-date="22"]'
    _MALE_RADIO_BTN = '//input[@value="male"]'
    _PRIVACY_POLICY_CHECKBOX = '//input[@name="gdpr_agree"]'
    _CREATE_ACC_BTN = '//input[@class="btn btn-success"]'
    _SUCCESS_PARAGRAPH_TEXT = '//[p]'

    def __init__(self, page):
        super().__init__(page)
        self.faker = Faker()
        self.email = self.faker.email()

    def fill_first_name(self):
        self.fill_input(self._FIRST_NAME_INPUT, self.faker.first_name())

    def fill_last_name(self):
        self.fill_input(self._LAST_NAME_INPUT, self.faker.last_name())

    def fill_email(self):
        self.fill_input(self._EMAIL_INPUT, self.email)

    def fill_re_email(self):
        self.fill_input(self._RE_EMAIL_INPUT, self.email)

    def fill_username(self):
        username = self.faker.user_name()
        self.fill_input(self._USERNAME_INPUT, username)
        return username

    def fill_password(self):
        password = self.faker.password()
        self.fill_input(self._PASSWORD_INPUT, password)
        return password

    def fill_birthday(self):
        self.click(self._BIRTHDAY_INPUT)
        birthdate = self.faker.date_of_birth(minimum_age=18, maximum_age=90)
        month = self.find(self._MONTH_PICKER)
        month.select_option(str(birthdate.month - 1))
        year = self.find(self._YEAR_PICKER)
        year.select_option(str(birthdate.year))
        day_xpath = f'//a[@data-date="{birthdate.day}"]'
        self.click(day_xpath)
        self.page.keyboard.type('Enter')

    def click_to_male_radiobutton(self):
        self.click(self._MALE_RADIO_BTN)

    def click_to_privacy_policy_checkbox(self):
        self.click(self._PRIVACY_POLICY_CHECKBOX)

    def click_create_account_button(self):
        self.click(self._CREATE_ACC_BTN)

    def check_success_text_after_registration(self):
        self.is_element_visible(self._SUCCESS_PARAGRAPH_TEXT)
