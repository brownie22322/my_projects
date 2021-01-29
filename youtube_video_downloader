from tkinter import*
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def download(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://en.savefrom.net')
    link_box = driver.find_element_by_xpath('//*[@id="sf_url"]')
    link_box.send_keys(link)

    download_button_1 = driver.find_element_by_xpath('//*[@id="sf_submit"]')
    download_button_1.click()

    time.sleep(10)

    download_button_2 = driver.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]/a')
    download_button_2.click()
    
root = Tk()
root.title('YouTube Video Downloader')
root.geometry('550x200')

title_label = Label(root, text = 'YouTube Video Downloader', font = '-family {Segoe UI} -size 20 -weight bold')
link_label = Label(root, text = 'Enter Link: ', font = '-family {Segoe UI} -size 13')
link_entry = Entry(root, width = 50)
download_button = Button(root, text = 'Download', font = '-family {Segoe UI} -size 13', command = lambda: download(link_entry.get()))

Label(root, text = '            ').grid(row = 0, column = 0)
title_label.grid(row = 0, column = 1)
Label(root, text = '            ').grid(row = 1, column = 0)
link_label.grid(row = 2, column = 0)
link_entry.grid(row = 2, column = 1)
Label(root, text = '            ').grid(row = 3, column = 0)
download_button.grid(row = 4, column = 1)

root.mainloop()
