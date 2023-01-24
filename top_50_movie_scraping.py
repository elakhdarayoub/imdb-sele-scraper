from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/user/chromedriver.exe')

# set google as your starting page and type in top 100 movies of all time in the box and press enter
driver.get('https://www.google.com')
sleep(5)
search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('top 100 movies of all time in the box', Keys.ENTER)

# click on the link corresponding to imdb
first_link = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/h3')
first_link.click()
# creat a wait time for the entire page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[3]/h3')))

# scroll all the way down to where the movie jaws appear
driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1300)')
sleep(5)
# take screen shot of the actual page, and get rid of the image of the jaws poster
page_screen = driver.save_screenshot('C:\\Users\\user\\Desktop\\screen.png')
poster_screen = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[50]/div[2]/a/img').screenshot('C:\\Users\\user\\Desktop\\moviePoster.png')
if page_screen and poster_screen:
    print('screenshots have been taken successfully')
else:
    print("somethinf went south, try again later")