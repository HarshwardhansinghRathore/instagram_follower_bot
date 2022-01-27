from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
import os

chrome_driver_path = 'C:\\Users\\hrath\\Downloads\\chromedriver_win32\\chromedriver.exe'

INSTAGRAM_ID = 'hr1566027'
INSTAGRAM_PASS_W = os.environ['PASSWORD']
similar_account = 'koenigsegg'


class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(4)
        my_id = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        my_id.send_keys(INSTAGRAM_ID)

        my_pass = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        my_pass.send_keys(INSTAGRAM_PASS_W)

        log_in_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in_btn.click()
        time.sleep(5)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()

        time.sleep(4)
        notification_not_now = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
        notification_not_now.click()
        time.sleep(5)

    def find_followers(self):
        search_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_input.send_keys(similar_account)
        time.sleep(5)
        koenigsegg_id = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        koenigsegg_id.click()
        time.sleep(4)
        koenigsegg_followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        koenigsegg_followers_link.click()
        time.sleep(4)
        scroll_up = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_up)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector('.PZuss div button')
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

koenigsegg_followers_follow = InstaFollowers()
koenigsegg_followers_follow.login()
koenigsegg_followers_follow.find_followers()
koenigsegg_followers_follow.follow()