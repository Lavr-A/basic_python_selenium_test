from selenium import webdriver
driver = webdriver.Chrome ("D:\\chromedriver.exe")
driver.get ("https://wikipedia.org/")

search_field = driver.find_element_by_id("searchInput").send_keys("Test Automation")
search_button = driver. find_element_by_xpath("//form[@id = 'search-form']/fieldset /button")
search_button.click()

element_field = driver.find_element_by_xpath("//a[@href='/wiki/Selenium']")
element_field.click()
assert "Selenium" in driver.title
driver.quit()
