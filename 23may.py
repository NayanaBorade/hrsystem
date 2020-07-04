from selenium import webdriver

driver =  webdriver.Chrome(executable_path = r"C:\Users\Amol\PycharmProjects\duringClass\resources\chromedriver.exe")

driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/")
loginusername = driver.find_element_by_id("loginname")
loginusername.send_keys("stc123")
print(type(loginusername))
my_tag_name = loginusername.tag_name
driver.find_element_by_id("loginpassword").send_keys("12345")
driver.find_element_by_id("loginbutton").click()
login_button = driver.find_element_by_id("loginbutton")
login_button.is_displayed()
login_button.is_selected()
login_button.text
mytext=driver.find_element_by_xpath("//label[@for='username']")
print(mytext.text)


#driver.quit() #close the browser