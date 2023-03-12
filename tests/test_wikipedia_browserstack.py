from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from mobile_tests.model import app


def test_wikipedia():
    with step('skip start screen'):
        app.given_opened()
    with step('Input search text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Programming')
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))
    with step('Check search results'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('An error occurred'))
    with step('Back to search screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_button')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Search Wikipedia'))
