from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
website_url = "https://htoh.asia/ru8cj4"
scroll_times = 5
scroll_interval = 0.5
driver = webdriver.Chrome()
driver.get(website_url)

for i in range(scroll_times):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(scroll_interval)
soup = BeautifulSoup(driver.page_source)

selector = "div.card mb-3 card-updates views rounded-large shadow-large card-border-0".replace(" ", '.')
for block in soup.select(selector):
    # get block title
    title_block = block.select('h5.update-title')
    if(len(title_block)>1):
        print(title_block[0].text)    

driver.close()
