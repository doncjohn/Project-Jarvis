from selenium import webdriver
driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
#Fetching the Details for sending message
name = input('Enter the name of user or group : ')
msg = input('Enter the message :')
#Opening the URL
driver.get('http://web.whatsapp.com')
#Scan the code before proceeding further
input('Enter anything after scanning QR code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys(msg)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
