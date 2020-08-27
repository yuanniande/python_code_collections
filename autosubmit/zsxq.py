import autoit

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
实现实时星球批量发帖
'''

def input_picture_path(path):
    autoit.control_send("打开", "Edit1", path)
    autoit.control_click("打开", "Button1")



chrome_options = Options()
browser = webdriver.Chrome(chrome_options=chrome_options)



import time

browser.set_window_size(828, 100)
browser.get('https://wx.zsxq.com/dweb2/index/group/init')
time.sleep(10)

upload_pic = browser.find_element_by_class_name('pic')
upload_pic.click()
time.sleep(1)
input_picture_path("C:\\Users\\yuanniande\\Desktop\\下载.png")

time.sleep(5)

textarea = browser.find_element_by_tag_name('textarea')
textarea.send_keys('test')

submitbtn = browser.find_element_by_class_name('submit-btn')
submitbtn.click()

#https://wx.zsxq.com/dweb2/index/group/init