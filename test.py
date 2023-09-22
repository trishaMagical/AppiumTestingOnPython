import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
#     language='en',
#     locale='US'
# )
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.hilmk.hilmkMyApp',
    appActivity='com.hilmk.hilmkMyApp.Activity.SplashActivity'
)
appium_server_url = 'http://localhost:4723'
class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        options = UiAutomator2Options()
        options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.driver.implicitly_wait(10)
        # self.driver = webdriver.Remote(appium_server_url, capabilities)
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    def test_find_battery(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()
    def test_anonymous_user(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="التنقل إلى أعلى"]')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/tvMenuUserIdValue')
        assert el.text.isnumeric() == True
        self.assertTrue(el.text.isnumeric())
    def test_ask_question_to_consultant(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnAddPostTop')
        el.click()
        els = self.driver.find_elements(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/tvPriceDescr')
        self.assertEqual(els[0].text, 'خدمة سريعة - 15 ريال سعودي')
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnNext')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnQuestionToSpecificConsultant')
        el.click()
        els = self.driver.find_elements(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/tvConsultantFullName')
        consultant_name = els[0].text
        els = self.driver.find_elements(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnPickConsultant')
        els[0].click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/spinnerGender')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.CheckedTextView[@text="ذكر"]')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnNext')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/etPostDescr')
        el.click()
        el.send_keys("abcde")
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/btnSubmitPost')
        el.click()
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/rvMyUnpickedQuestionsList')
        self.assertTrue(el.is_displayed())
        els = self.driver.find_elements(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/tvQuestionDescr')
        self.assertEqual(els[0].text, "abcde")
        els = self.driver.find_elements(
            by=AppiumBy.ID, value='com.hilmk.hilmkMyApp:id/tvConsultantFullName')
        self.assertEqual(els[0].text, consultant_name)
if __name__ == '__main__':
    unittest.main()