from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome(r"C:\Users\rajni\Desktop\Whatsapp\whazzap\chromedriver") 

driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(600) 
wait = WebDriverWait(driver, 600) 
time.sleep(3)
print("Wait Over")
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Nitish Jio"'

# Replace the below string with your own message 
string = "Message sent using Python!!!"
time.sleep(3)
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg)))
time.sleep(3)    
group_title.click()
print("Group Title clicked\t")


#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
#input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
inp_xpath.click()
print(inp_xpath)
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath)))

for i in range(2): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1)

