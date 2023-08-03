# from selenium import webdriver
# from selenium.webdriver.common import keys
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
#
# def x(u=None):
# 	if u == None:
# 		return
# 	u = u.split(",")
# 	act_value = ""
# 	for value in u:
# 		if not value == " Kelambakkam" and not value == " Tamil Nadu 603103" and not value[0]=="Q" and not value[0]=="R":
#
# 			act_value += value
# 	return act_value
#
# driver = webdriver.Chrome()
# driver.get("http://www.google.com")
# driver.maximize_window()
# elem = driver.find_element(By.CLASS_NAME,"gLFyf")
# elem.send_keys("atm in kelambakkam")
# elem.send_keys(Keys.RETURN)
# time.sleep(2)
# elem = driver.find_element(By.CLASS_NAME,"Z4Cazf")
# elem.click()
# time.sleep(2)
#
#
# while True:
# 	elems = driver.find_elements(By.CLASS_NAME, "dbg0pd")
# 	for element in elems:
# 		element.click()
# 		time.sleep(5)
# 		el = driver.find_element(By.CLASS_NAME,"SPZz6b")
# 		elem = driver.find_element(By.CLASS_NAME,"LrzXr")
#
# 		print(element.text+"       "+x(elem.text))
# 		# import requests
# 		# response = requests.post("http://192.168.138.141:8000/shop",data={
# 		#     "name":element.text,
# 		# 	"fro_m":elem.text
# 		# })
# 		# print(response.status_code)
# 	try:
# 		elem = driver.find_element(By.XPATH, "//*[@id='pnnext']/span[2]")
# 		elem.click()
# 	except:
# 		break
# 	time.sleep(5)
# time.sleep(1)
# elem.click()
# time.sleep(10)
#
#
#
#
#
#
megnha=input()
if (megnha=="died"):
    print ("surya meets priya")
else:
    print("surya weds megnha")