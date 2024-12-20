import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
time.sleep(3)
loginName = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
loginName.send_keys("Admin")

loginPassword = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
loginPassword.send_keys("admin123")

loginButton = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
loginButton.click()

add_candidate = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]")))
add_candidate.click()
time.sleep(5)
vartotojo_tikras_vardas = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
vartotojo_tikras_vardas.send_keys("Ugnius")
time.sleep(5)
middle_name = wait.until(EC.presence_of_element_located((By.NAME, "middleName")))
middle_name.send_keys("Bugnius")
time.sleep(5)
last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
last_name.send_keys("Brazauskas")
time.sleep(5)
vacancy = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")))
vacancy.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Payroll Administrator')]").click()
time.sleep(2)
time.sleep(5)
email = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")))
email.send_keys("test@gmail.com")
time.sleep(5)
phone_number = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]")))
phone_number.send_keys("112")
time.sleep(5)
file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys("C:/Users/justi/Downloads/wfevs.docx")
time.sleep(5)
submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[8]/button[2]")))
submit.click()
time.sleep(5)
shortlist = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/button[2]")))
shortlist.click()
time.sleep(3)
time.sleep(5)
notes = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea[1]")))
notes.send_keys("Test123test 11 2")
time.sleep(5)
submit2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]")))
submit2.click()
time.sleep(5)
submit3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/button[2]")))
submit3.click()
time.sleep(5)
interview_title = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")))
interview_title.send_keys("Thomas Kutty Benny")
time.sleep(5)
time.sleep(3)

birth_date = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/input[1]")))
birth_date.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
birth_date.send_keys("1990-11-12")
time.sleep(5)
# /html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input
set_time = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/input[1]")))
set_time.send_keys("6:50")


inter = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input")))
inter.send_keys("aaa aaa")


time.sleep(5)
notes2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[5]/div[1]/div[2]/textarea[1]")))
notes2.send_keys("Krabas Labas labas 123")
time.sleep(5)
submit4 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]")))
submit4.click()
time.sleep(5)

time.sleep(100)