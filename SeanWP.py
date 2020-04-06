from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\SeanMac\\Selenium\\chromedriver.exe")

driver.get("http://www.killertechwolf.com/WordPressPages/sean")

driver.maximize_window()

print(len(driver.find_elements_by_class_name('popup.cboxElement')))

def test_page(linkname):
    driver.find_element_by_link_text(linkname).click()
    time.sleep(3)
    driver.find_element_by_id("colorbox").click()
    time.sleep(7)
    driver.find_element_by_id("colorbox").click()
    time.sleep(3)
    driver.execute_script("$('#cboxOverlay').css('visibility', 'hidden');")
    driver.execute_script("$('#colorbox').css('visibility', 'hidden');")
    time.sleep(2)

vids=driver.find_elements_by_class_name('popup.cboxElement')

for vid in vids:
    test_page(vid.text)

driver.close()