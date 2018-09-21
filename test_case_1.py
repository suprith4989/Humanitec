from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(profile)

driver.get("https://www.ultimateqa.com/filling-out-forms/")
driver.maximize_window()
assert "Ultimate QA" in driver.title

element1 = driver.find_element_by_id('et_pb_contact_name_1')
element1.clear()
element1.send_keys("Suprith Gangawar")

element2 = driver.find_element_by_id('et_pb_contact_message_1')
element2.clear()
element2.send_keys("Test Message")

#element3 = driver.find_element_by_xpath("//div[@id='et_pb_contact_form_0']//button[@type='submit'][contains(text(),'Submit')]")
element3 = driver.find_element_by_xpath("//div[@class='et_contact_bottom_container']")
element3.click()

try:
    element4 = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Form filled out successfully')]"))).text
    assert "Form filled out successfully" in element4
finally:
    driver.quit()
