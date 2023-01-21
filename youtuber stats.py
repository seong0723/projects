from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

#use socialblade.com/youtube to search up any youtuber and extract data to observe
#their number of subscribers, video uploads, total views, youtube link, etc.


def get_url(search_youtuber):
    template = "https://socialblade.com/youtube/user/{}"
    search_youtuber = search_youtuber.replace(' ', '+')

    #add term query to url
    url = template.format(search_youtuber)
    return url



def find_data(youtuber):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    url = get_url(youtuber)
    driver.get(url)
    name = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlockTop"]/div[1]/h1').text
    button = driver.find_element(By.CSS_SELECTOR, 'a.-margin')
    link = button.get_attribute('href')
    sub_count = driver.find_element(By.XPATH,'//*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]').text
    driver.quit

    return ("Name: "+ name, "Subscribers: " + sub_count, "Youtube Link: " + link)

print(find_data('pewdiepie'))
