from selenium import webdriver
from selenium.webdriver.common import options
import time

def get_driver():
  #Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-inforbars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  #Tách text và số từ text
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  
  #Thời gian chờ để sang trang và lấy text + Dynamic value
  time.sleep(2)
  
  #Điền link xpath vào value, dùng copy full xpath
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())
