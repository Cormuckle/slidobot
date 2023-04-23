from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import sys
import getopt
from webdriver_manager.chrome import ChromeDriverManager

EVERYONE = [2,3,5,6]
class SlidoBot:
    def __init__(self, hash=None, xpath=None, driver=None, who=1):
        self.driver = driver
        self.who = who
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        self.driver.get("https://app.sli.do/event/bsTUZCsBZLNMuByJMnbjhd/live/polls")
        time.sleep(1.7)
        click_elem = self.driver.find_element(By.CSS_SELECTOR,"#live-tabpanel-polls > div > div > div > form > div:nth-child(1) > div > div.poll-question__body-container > div > div.poll-question__body > div > label:nth-child("+str(self.who)+")")
        click_elem.click()
        time.sleep(.25)
        submit = self.driver.find_element(By.CSS_SELECTOR, "#poll-submit-button")
        submit.click()
        time.sleep(.75)

# hash # xpath # times
def main():


    for i in range(1, int(500)+1):
        BOT = SlidoBot( who= EVERYONE[i%4])
        BOT.vote()
        BOT.closeBrowser()
        print("Votes: " + str(i))
if __name__ == "__main__":
    print("Have fun.")
    main()