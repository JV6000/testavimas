import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# launch application
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/definePredefinedReport")

driver.maximize_window()


name = wait.until(EC.presence_of_element_located((By.NAME, "username")))
name.send_keys("Admin")

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("admin123")

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

report_name = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")))
report_name.send_keys("TEST123")

select_criteria_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
select_criteria_1.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Education')]").click()
time.sleep(2)

submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]")))
submit.click()

select_criteria_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
select_criteria_2.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Job Title')]").click()
time.sleep(2)

submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]")))
submit.click()

which_education =  wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]")))
which_education.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'High School Diploma')]").click()
time.sleep(2)

what_job =  wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]")))
what_job.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'IT Manager')]").click()
time.sleep(2)

include =  wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")))
include.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Current and Past Employees')]").click()
time.sleep(2)


group_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
group_1.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Personal')]").click()
time.sleep(2)
submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/i[1]")))
submit.click()


group_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
group_2.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Contact Details')]").click()
time.sleep(2)
submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/i[1]")))
submit.click()

group_3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
group_3.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Salary')]").click()
time.sleep(2)
submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/i[1]")))
submit.click()

group_4 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
group_4.click()
driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Immigration')]").click()

submit = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/i[1]")))
submit.click()

include_header1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[5]/div[1]/label[1]/span[1]")))
include_header1.click()

include_header2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[8]/div[1]/label[1]/span[1]")))
include_header2.click()

include_header3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[11]/div[1]/label[1]/span[1]")))
include_header3.click()

include_header4 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[14]/div[1]/label[1]/span[1]")))
include_header4.click()


delete1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[4]/div[1]/span[1]/i[1]")))
delete1.click()
time.sleep(2)

delete2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[4]/div[1]/span[2]/i[1]")))
delete2.click()
time.sleep(2)

delete3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[4]/div[1]/span[3]/i[1]")))
delete3.click()

delete_row = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[9]/button[1]/i[1]")))
delete_row.click()

save = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/button[2]")))
save.click()




time.sleep(20)