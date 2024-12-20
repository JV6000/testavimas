import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")

driver.maximize_window()

time.sleep(5)
name = wait.until(EC.presence_of_element_located((By.NAME, "username")))
name.send_keys("Admin")

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("admin123")
time.sleep(5)
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()
time.sleep(5)
"""
create_login_details = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")))
create_login_details.click()
"""
file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys("C:/Users/justi/PycharmProjects/testavimas/200x200.jpg")
time.sleep(5)
vartotojo_tikras_vardas = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
vartotojo_tikras_vardas.send_keys("jonas")
time.sleep(5)
middle_name = wait.until(EC.presence_of_element_located((By.NAME, "middleName")))
middle_name.send_keys("jonautas")
time.sleep(5)
last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
last_name.send_keys("Erlickas")
time.sleep(5)
employee_id = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]")))
employee_id.send_keys("6")
time.sleep(5)
"""
employee_username = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")))
employee_username.send_keys("Ju11o3z2a211pa1s")

employee_password = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
employee_password.send_keys("labasrytas123")

employee_password_confirm = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[2]")))
employee_password_confirm.send_keys("labasrytas123")
"""
time.sleep(5)
add_job = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
add_job.click()
"""    """
time.sleep(5)
go_to_job = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]")))
go_to_job.click()
time.sleep(5)

joined_date = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))
joined_date.send_keys("1990-12-12")
time.sleep(5)

job_title = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")))
job_title.send_keys("a")
time.sleep(5)

job_category =  wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]")))
job_category.send_keys("Craft Workers")
time.sleep(10)

sub_unit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]")))
sub_unit.click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Administration')]").click()
time.sleep(5)

location = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]")))
location.send_keys("Canadian Regional HQ")
time.sleep(5)

employment_status = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]")))
employment_status.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Full-Time Permanent')]").click()
time.sleep(5)

report_to = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/a[1]')
report_to.click()
time.sleep(5)

addSupervisor = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]")
addSupervisor.click()
time.sleep(5)
supervisors_name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
supervisors_name.send_keys("Odis Adalwin")
time.sleep(5)
report_method = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")))
report_method.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Direct')]").click()
time.sleep(5)



time.sleep(100)

# driver.quit