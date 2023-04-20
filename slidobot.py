from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import getopt

class SlidoBot:
    def __init__(self, hash=None, xpath=None, driver=None):
        self.driver = driver
        
        self.driver = webdriver.Chrome(self.driver)
    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        self.driver.get("https://app.sli.do/event/bsTUZCsBZLNMuByJMnbjhd/live/polls")
        time.sleep(1.5)
        click_elem = self.driver.find_element(By.CSS_SELECTOR,"#live-tabpanel-polls > div > div > div > form > div:nth-child(1) > div > div.poll-question__body-container > div > div.poll-question__body > div > label:nth-child(1)")
        click_elem.click()
        time.sleep(.25)
        submit = self.driver.find_element(By.CSS_SELECTOR, "#poll-submit-button")
        submit.click()
        time.sleep(.75)

# hash # xpath # times
def main():

    try:
        options, args = getopt.getopt(
            sys.argv[1:], "-d:",
            ["driver="])
        for name, value in options:
            if name in ('-d', '--driver'):
                print(value)
                DRIVER = value 

    except getopt.GetoptError as err:
        print(str(err))
        print("Invalid args!")
        sys.exit(1)

    for i in range(1, int(15)+1):
        BOT = SlidoBot(driver= DRIVER)
        BOT.vote()
        BOT.closeBrowser()
        print("Votes: " + str(i))
if __name__ == "__main__":
    print("Have fun.")
    main()