
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
time.sleep(5)
loginName = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
loginName.send_keys("Admin")

loginPassword = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
loginPassword.send_keys("admin123")

loginButton = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
loginButton.click()
time.sleep(5)

employee_id = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")))
employee_id.send_keys("03107")

press_search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")))
press_search.click()
time.sleep(5)

press_employee = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]")))
press_employee.click()

time.sleep(5)


vartotojo_tikras_vardas = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
vartotojo_tikras_vardas.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
vartotojo_tikras_vardas.send_keys("Juozas")

time.sleep(5)
middle_name = wait.until(EC.presence_of_element_located((By.NAME, "middleName")))
middle_name.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
middle_name.send_keys("Tomashas")

last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
last_name.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
last_name.send_keys("Erlickas")

other_ID = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]")))
other_ID.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
other_ID.send_keys("123")


driver_license_number = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")))
driver_license_number.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver_license_number.send_keys("123")
time.sleep(5)
nationality = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
nationality.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Lithuanian')]").click()
time.sleep(5)

martial_status = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")))
martial_status.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Single')]").click()
time.sleep(2)

birth_date = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))
birth_date.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
birth_date.send_keys("1990-11-12")
time.sleep(5)

male_female = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]")))
male_female.click()
time.sleep(5)
save_main_info = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")))
save_main_info.click()

time.sleep(5)
""" 2a forma"""


blood_type = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
blood_type.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'A+')]").click()
time.sleep(2)

test_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")))
test_field.send_keys("test123321")
time.sleep(2)
save_main_info2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/button[1]")))
save_main_info2.click()

time.sleep(2)
""" 3a forma failai """
add_files_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]")))
add_files_button.click()
time.sleep(2)
file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys("C:/Users/justi/PycharmProjects/testavimas/200x200.jpg")
time.sleep(2)
save_main_info3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/button[2]")))
save_main_info3.click()
time.sleep(2)
add_files_button1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]")))
add_files_button1.click()
time.sleep(2)
file_input1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input1.send_keys("C:/Users/justi/PycharmProjects/testavimas/200x200.jpg")
time.sleep(2)
save_main_info31 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/button[2]")))
save_main_info31.click()
time.sleep(2)
download_photo1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/button[3]/i[1]")))
download_photo1.click()
time.sleep(2)

download_photo2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/button[3]/i[1]")))
download_photo2.click()
time.sleep(2)

delete_photo1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/button[2]/i[1]")))
delete_photo1.click()
time.sleep(2)

confirm_delete1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]")))
confirm_delete1.click()
time.sleep(10)

delete_photo2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/button[2]/i[1]")))
delete_photo2.click()
time.sleep(5)

confirm_delete1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]")))
confirm_delete1.click()
time.sleep(10)

time.sleep(100)