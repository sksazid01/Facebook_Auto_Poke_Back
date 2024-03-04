import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("") #Facebook Link here
time.sleep(1)



m_mail = driver.find_element(By.ID,"m_login_email")
m_pass = driver.find_element(By.CLASS_NAME,"bf.bg.bi.bj")
login = driver.find_element(By.CLASS_NAME,"bk.bl.bm.bn.bo.bp")
m_mail.send_keys("") #Facebook login mail
m_pass.send_keys("") #Facebook password
login.submit()

time.sleep(2)

for it in range(1,2000):
   #poke Link provide here.
   driver.get("Poke link here") #link for each person
   driver.get("Poke link here") #link for each person
    
driver.quit()
