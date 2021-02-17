from selenium import webdriver
driver = webdriver.Chrome ("D:\Лекции IT Academy\Chrome\chromedriver.exe")
driver.get ("https://wikipedia.org/")

search_field = driver.find_element_by_id("searchInput").send_keys("Space")
search_button = driver. find_element_by_xpath("//form[@id = 'search-form']/fieldset /button")
search_button.click()

assert "Space" in driver.title
driver.quit()
