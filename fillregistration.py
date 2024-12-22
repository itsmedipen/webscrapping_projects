
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



website = 'https://sample.technologychannel.org/sample_registration_form'
driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
first_name = driver.find_element(By.ID,"first-name")
first_name.send_keys('Dipen')
last_name = driver.find_element(By.ID,"last-name")
last_name.send_keys('Sherpa')
email = driver.find_element(By.ID,"email")
email.send_keys('dipensherpa5@gmail.com')
phone_num = driver.find_element(By.ID,"phone")
phone_num.send_keys('9843590714')
dob = driver.find_element(By.ID,"dob")
dob.send_keys('12/11/2020')
gender = driver.find_element(By.NAME,"gender")
gender.send_keys('Male')
time.sleep(5)
gender.click()
select_course = driver.find_element(By.ID,"course")
time.sleep(2)
select_course.send_keys("Python Programming")
time.sleep(10)
address = driver.find_element(By.ID,"address")
address.send_keys('Bouddha, Kathmandu')
time.sleep(2)
password = driver.find_element(By.ID,"password")
password.send_keys('dipensherpa123')
confirm_password = driver.find_element(By.ID,"confirm-password")
confirm_password.send_keys('dipensherpa123')
time.sleep(5)
check_box = driver.find_element(By.ID,"terms")
check_box.click()
time.sleep(2)
button = driver.find_element(By.XPATH,'//*[@id="registrationForm"]/div[12]/button')
button.click()
time.sleep(50)
