from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(chrome_options=chrome_options)


def capture_page(url, path, name='screenshot'):
    if not os.path.exists(path):
        os.mkdir(path)
    browser.set_window_size(828, 100)
    try:
        browser.get(url)
    except Exception as e:
        print(url)
        #print(url)
        #raise xf
    browser.implicitly_wait(1)
    height = browser.execute_script("return document.documentElement.scrollHeight")
    #time.sleep(3)
    browser.set_window_size(828, height)
    pic_name = name+'.png'
    pic_path = os.path.join(path, pic_name)
    browser.save_screenshot(pic_path)
    #browser.quit()





if __name__ == '__main__':
    for path, dir_list, file_list in os.walk('../processed/'):
        for file_name in file_list:
            if 'html' in file_name and 'png' not in file_name:
                capture_page('file:///'+os.path.abspath(path+file_name), path, file_name)
        break