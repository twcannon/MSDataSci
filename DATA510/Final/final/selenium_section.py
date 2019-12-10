import selenium
from selenium import webdriver
import time


###### SELENIUM SECTION

browser = webdriver.Chrome("/home/thomas/git/datascience/MSDataSci/DATA510/projects/FirstDjangoProject/driver/chromedriver")

browser.get('https://www.alltrails.com/us/south-carolina')
for el in range(3):
    browser.find_elements_by_xpath("//div[@class='feed-item load-more trail-load']")[0].click()
    time.sleep(5)

allTrails = browser.find_elements_by_xpath("//div[@class='item-info']")

print('\n\n********4.5-star Trails********')
for trail in allTrails:
    if trail.find_elements_by_class_name('star_4-5'):
        print(trail.find_elements_by_tag_name('span')[-1].text)
print('\n\n********4-star Trails********')
for trail in allTrails:
    if trail.find_elements_by_class_name('star_4'):
        print(trail.find_elements_by_tag_name('span')[-1].text)
print('\n\n********3.5-star Trails********')
for trail in allTrails:
    if trail.find_elements_by_class_name('star_3-5'):
        print(trail.find_elements_by_tag_name('span')[-1].text)