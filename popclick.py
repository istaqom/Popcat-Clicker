from selenium import webdriver

url = "https://popcat.click/"

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get(url)

while True:
    driver.find_element_by_tag_name('body').click()