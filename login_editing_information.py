"""
Author:jyothsna
modified date:07/07/2020

"""

import time
from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
"""login to account and editing information in history,physical examination and diagnosys"""
driver=webdriver.Chrome()
#getting url
driver.get("https://www.charmhealth.com/")
#maximize windows
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Login']").click()
driver.find_element_by_xpath("//input[@id='lid']").send_keys("dev+5@deepscribe.ai")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys('vgS9Y3RDhq2tnhE')
driver.find_element_by_xpath("//div[@id='signin_submit']").click()
driver.find_element_by_xpath("//i[@id='NEW_DIALOG_CLOSE_MARK']").click()
driver.find_element_by_xpath("//i[@class='charts-menu-icon']").click()
driver.find_element_by_xpath("//tbody[@id='chartRecords']/tr/td[contains(text(),'In Person')]").click()
driver.find_element_by_xpath("//button[text()='Edit']").click()
driver.find_element_by_xpath("//div[text()='History']").click()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='ze_area']"))
# ## Insert text via xpath #

elem = driver.find_element_by_xpath("/html/body/div")
# # updating the data for history
elem.send_keys("Patient presents today for concerns regarding his palpitations, but nothing he thinks is serious. ")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//div[text()='Physical Examination']")))
element.click()
driver.find_element_by_xpath("//div[text()='Physical Examination']").click()
time.sleep(1)
driver.find_element_by_xpath("(//div[text()='Templates'])[2]").click()
wi=driver.window_handles
driver.switch_to_window(wi[0])
try:
 driver.find_element_by_xpath("//div[@id='lftContainer']/ul/ul/li[47]").click()
except ElementClickInterceptedException:
 driver.find_element_by_xpath("(//input[@type='checkbox'])[18]").click()
driver.find_element_by_xpath("//label[text()='lesion']").click()
driver.find_element_by_xpath("//label[text()='color']").click()
driver.find_element_by_xpath("//label[text()='blue']").click()
driver.find_element_by_xpath("(//div[@class='mentions-input-box'])[3]/input").send_keys("70mm")

driver.find_element_by_xpath("//div[text()='Add Dx']").click()

win=driver.window_handles
time.sleep(1)
driver.switch_to_window(win[0])
driver.find_element_by_xpath("//input[@name='diagnosis_0']").send_keys("Hypertension")
try:
    driver.find_element_by_xpath("(//span[text()='Hypertension'])[1]").click()
except ElementClickInterceptedException:

 driver.find_element_by_xpath("//button[text()='Add']").click()
driver.close()






#
