from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import json

def scroll_to_buttom(driver, scroll_times=10, scroll_interval=1):
    for _ in range(scroll_times):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(scroll_interval)

def get_every_file(soup):
    # get every post info
    data_dict = dict()
    selector = "div.card mb-3 card-updates views rounded-large shadow-large card-border-0".replace(" ", '.')
    for block in soup.select(selector):
        title_block = block.select('h5.update-title')
        title = ""
        if(len(title_block)>0):
            title = title_block[0].text
        else:
            title = "no title"
        print(title)

        header_block = block.select("img.lazyloaded")
        header = ""
        if(len(header_block)>0):
            print(header_block)
            header = header_block[0].src
            header = header_block
        else:
            header = "no header"
        print(header)

        each_file_selector = "a.media-wrapper rounded-0 saveclick glightbox".replace(" ", ".")
        file_block = block.select(each_file_selector)
        file_list = []
        if(len(file_block)>0):
            # print(file_block)
            for link in file_block:
                # print(link)
                link = link.attrs['href']
                print(link)
                file_list.append(str(link))
        else:
            print("cannot get file")

        data_dict[str(title)] = [str(header), file_list]
    return data_dict

def save_file(path, html):
    with open(path, 'w', encoding="utf-8") as f:
        f.write(html)

def login(driver, username, password, url):
    driver.get(url)
    driver.find_element(By.ID,'username_email_input').send_keys(username)
    driver.find_element(By.NAME,'password').send_keys(password)
    driver.find_element(By.NAME,'password').send_keys(Keys.ENTER)

if __name__ == "__main__":
    website_url = "https://htoh.asia/"
    login_url = "https://htoh.asia/login"
    username = "" # gmail
    password = "" # password

    scroll_times = 20
    scroll_interval = 1
    # driver init
    driver = webdriver.Chrome()
    
    login(driver, username, password, login_url)
    sleep(3)
    
    driver.get(website_url)
    scroll_to_buttom(driver, scroll_times, scroll_interval)

    soup = BeautifulSoup(driver.page_source, features="html.parser")
    
    data_dict = get_every_file(soup)
    save_file("all_file_info.json", json.dumps(data_dict))

    driver.close()
