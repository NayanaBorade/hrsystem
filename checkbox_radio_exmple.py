from selenium import webdriver

driver =  webdriver.Chrome(executable_path = r"C:\Users\Amol\PycharmProjects\duringClass\resources\chromedriver.exe")
print(type(driver))
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/")