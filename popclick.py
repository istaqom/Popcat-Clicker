from selenium import webdriver

url = "https://popcat.click/"

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get(url)
id = driver.find_element_by_tag_name('body')
while True:
    try:
        id.click() 
    except Exception as ex: # until it breaks
        print('Time is over')
        break
    