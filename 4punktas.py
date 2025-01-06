from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
loginName = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
loginName.send_keys("Admin")

loginPassword = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
loginPassword.send_keys("admin123")

loginButton = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
loginButton.submit()
time.sleep(2)

buzzClick = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
buzzClick.click()
time.sleep(5)
text = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/textarea')
text.send_keys("labas")


clickAddPhoto = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/button[1]')
clickAddPhoto.click()
time.sleep(2)
file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys("C:/Users/justi/PycharmProjects/testavimas/200x200.jpg")
time.sleep(2)
upload = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[3]/button')
upload.click()
time.sleep(3)

heart = driver.find_element(By.XPATH, '//*[@id="heart"]')
heart.click()
time.sleep(5)

editMsg = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button/i')
editMsg.click()
time.sleep(5)
option = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//*[text()='Edit Post']"))
)
option.click()

time.sleep(5)


editedMsg = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/ul/li[2]/p')
editedMsg.send_keys("labas")

post = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[3]/button')
post.click()
time.sleep(2)
comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[1]/i')
comment.click()

commentWord = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div/form/div/div[2]/input')
commentWord.send_keys("labas")
commentWord.send_keys(Keys.ENTER)
time.sleep(2)
likeComment = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/div[2]/div[2]/p[1]')
likeComment.click()
time.sleep(2)
editedMsg1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/div[2]/div[2]/p[2]')))
editedMsg1.click()
time.sleep(2)
editedMsg2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/div[2]/form/div/div[2]/input')
editedMsg2.send_keys("labas")
editedMsg2.send_keys(Keys.ENTER)
time.sleep(2)
delComment = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/div[2]/div[2]/p[3]')
delComment.click()
time.sleep(2)
confirmDel = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
confirmDel.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)
delMsg = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button/i')
delMsg.click()

option = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//*[text()='Delete Post']"))
)
option.click()

time.sleep(1)
confirmDel1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
confirmDel1.click()
time.sleep(555)