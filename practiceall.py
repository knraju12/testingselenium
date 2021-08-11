from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome('Chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)

name_xpath = '//input[@id="name"]'
phone_xpath = '//input[@id="phone"]'
email_xpath = '//input[@id="email"]'
pass_xpath = '//input[@id="password"]'
address_xpath = '//*[@id="address"]'
login_xpath = '//button[@name="submit"]'

gender_xpath = '//input[@id="male"]'
which_day = '//input[@id="tuesday"]'
which_day1 = '//input[@id="friday"]'

browser.find_element_by_id('name').send_keys('knraj2')
time.sleep(2)
browser.find_element_by_id('phone').send_keys('9052950212')
time.sleep(2)
browser.find_element_by_id('email').send_keys('natrajmsd@gmail.com')
time.sleep(2)
browser.find_element_by_id('password').send_keys('Istra@24')
time.sleep(2)
browser.find_element_by_id('address').send_keys('')
time.sleep(2)
browser.find_element_by_name('submit').click()
time.sleep(2)

browser.find_element_by_id('male').click()
time.sleep(2)
browser.find_element_by_id('tuesday').click()
time.sleep(2)
browser.find_element_by_id('friday').click()
time.sleep(2)

sel = Select(browser.find_element_by_xpath("//select[@class='custom-select']"))
sel.select_by_visible_text("Norway")
time.sleep(2)

browser.find_element_by_xpath('//input[@type="radio"]/following-sibling::*[contains(.,"2")]').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@id="selenium"]/following-sibling::*').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@id="testng"]/following-sibling::*').click()
time.sleep(2)

browser.close()
