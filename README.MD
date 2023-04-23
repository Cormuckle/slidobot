# Sli.do voter bot useage #

This bot is designed to vote for you in sli.do polls. It is currently set to vote on one poll but can easily be adjusted. This bot was taken from [4rts](https://github.com/4rts/slido-bot/blob/master/slidobot.py) but has been edited to be easier to use for this specific poll and to use css selectors instead of xpaths. 

**I will show two ways to run this**


## Using executable ##
**This will not work on Windows**

First you can use the executable in the dist folder. 
Steps are as follows.

1. download the slidobot executable located in the dist folder
2. open terminal 
3. if on mac run "cd Downloads"
3. run "./slidobot"
4. enjoy

---

## Using Python3 ##

to use the python code you will need [Brew](https://brew.sh/) installed if you are on mac.

From there the steps are as follows:

1. Download slidobot.py and requirements.txt from this repo. To do this click the green CODE button and select "download zip"
2. open your terminal.
3. run "brew install python3"
4. the previous step should also install pip. if it doesn't then you will need to google how to install it.
5. run "CD ~"  to get to your home directory
6. run "CD Downloads"
7. run "unzip slidobot-master.zip"
8. run "cd slidobot-master"
9. run "pip install -r requirements.txt"
10. run "python3 slidobot.py"
11. enjoy your free votes

--- 

## editing functionality ##

on line 17 you can edit the option you want to vote on by changing the 1 in "label:nth-child(1)" to whichever option you want to select.

you can also change the number of votes you cast on line 41. change "int(15)" to "int(whatever you want)"

Finally. to use this for a different poll change the URL on line 15 to the one you want to use