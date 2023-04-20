# Sli.do voter bot useage #

This bot is designed to vote for you in sli.do polls. It is currently set to vote on one poll but can easily be adjusted. This bot was taken from [4rts](https://github.com/4rts/slido-bot/blob/master/slidobot.py) but has been edited to be easier to use for this specific poll and to use css selectors instead of xpaths. 

**I will show two ways to run this**


## Using executable ##

First you can use the executable in the dist folder. I have no idea what systems it works on or if your computer will be happy about you running it. It does require less setup though.

Steps are as follows.

1. Download [chromedriver](https://chromedriver.chromium.org/)
2. download the slidobot executable located in the dist folder
3. open terminal
4. run "CD Downloads" followed by "unzip "name of the chromedriver.zip you downloaded"" 
5. The unzipped version of the file should have the same name without the .zip so run "CD "Name of that file"" followed by PWD. Copy this output to your clipboard or wherever you can get at it easily
6. The executable should be in the Downloads folder of your laptop so run "CD ~/Downloads" 
7. finally run "./slidobot -d "Output/from/pwd/in/quotes/with/chromedriver/added/to/end""
8. enjoy

---

## Using Python3 ##

to use the python code you will need [Brew](https://brew.sh/) installed.

From there the steps are as follows:

1. open your terminal.
2. run "brew install python3"
3. the previous step should also install pip. if it doesn't then you will need to google how to install it.
4. Download [chromedriver](https://chromedriver.chromium.org/)
5. Download slidobot.py and requirements.txt from this repo
6. if you download these files directly they should be in the Downloads folder. if not you may have to figure out where they are. if you cloned this repo or forked it then you should know where they are. Locate them.
7. run "CD ~"  to get to your home directory
8. if you are in your home directory (should be a ~) then run "CD Downloads" followed by "unzip "name of the chromedriver.zip you downloaded"" 
9. The unzipped version of the file should have the same name without the .zip so run "CD "Name of that file"" followed by PWD. Copy this output to your clipboard or wherever you can get at it easily
10. Navigate back to the space where you stored the slidobot.py and requirements.txt (Use cd ~ to get back to home directory or cd .. to move back by one directory)
11. run "pip install -r requirements.txt"
12. finally run "python3 slidobot.py -d "Output/from/pwd/in/quotes/with/chromedriver/added/to/end"" 
13. sit back and enjoy

--- 

## editing functionality ##

on line 17 you can edit the option you want to vote on by changing the 1 in "label:nth-child(1)" to whichever option you want to select.

you can also change the number of votes you cast on line 41. change "int(15)" to "int(whatever you want)"

Finally. to use this for a different poll change the URL on line 15 to the one you want to use