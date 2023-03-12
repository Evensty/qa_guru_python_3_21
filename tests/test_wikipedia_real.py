from allure import step
import allure

from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser

from mobile_tests.model import app

def test_wikipedia():
    with step('skip start screen'):
        app.given_opened()
    with step('add a language'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_icon')).click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[1].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[0].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[1].click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/section_header_text')).should(have.text('Your languages'))
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[3].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[3].click()
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')).should(have.size_greater_than(1))
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

