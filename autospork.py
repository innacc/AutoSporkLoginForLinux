
#!/usr/bin/env python
import os
import selenium
import time
import datetime
from datetime import date
import calendar
from selenium import webdriver
from playsound import playsound
home = os.path.expanduser("~")

### INPUT YOUR CREDENTIALS HERE ###

if(os.stat(home+"/autosporklogin/Login.txt").st_size == 0):
    print("              _                             _    ")
    print("   __ _ _   _| |_ ___  ___ _ __   ___  _ __| | __")
    print("  / _` | | | | __/ _ \/ __| '_ \ / _ \| '__| |/ /")
    print(" | (_| | |_| | || (_) \__ \ |_) | (_) | |  |   < ")
    print("  \__,_|\__,_|\__\___/|___/ .__/ \___/|_|  |_|\_\ ")
    print("                            |_|                    ")
    print("welcome to autosporklogin")
    time.sleep(3)
    print("Make sure firefox is installed")
    time.sleep(3)
    print("a donation to the paypal isaac.don7@gmail.com would be nice, but it is not necessary")
    time.sleep(3)
    print("I am not resposible if this tool does not work")
    time.sleep(3)
    print("if you have less than 7 classes this will not work")
    print("please enter username")
    userid = input()
    print("please enter password")
    passid = input()
    print("do you have 8 classes (0 and 8th period with no free periods) (Yes/No (make sure the Y or N are capital))")
    zeroeight = input()
    
    usernameid = userid
    passwordid = passid
    zeroandeight = zeroeight
    

    f = open(home+"/autosporklogin/Login.txt", "a")
    f.write("%s"% userid+"\n")
    f.write("%s"% passid+"\n")
    f.write("%s"% zeroeight)
    f.close()
else:
    print("              _                             _    ")
    print("   __ _ _   _| |_ ___  ___ _ __   ___  _ __| | __")
    print("  / _` | | | | __/ _ \/ __| '_ \ / _ \| '__| |/ /")
    print(" | (_| | |_| | || (_) \__ \ |_) | (_) | |  |   < ")
    print("  \__,_|\__,_|\__\___/|___/ .__/ \___/|_|  |_|\_\ ")
    print("                            |_|                    ")
    f = open(home+"/autosporklogin/Login.txt", "r")
    usernameid = f.readlines(1)
    passwordid = f.readlines(2)
    zeroandeight = f.readlines(3)

# checks if it is saturday or sunday
my_date = date.today()
currentday = calendar.day_name[my_date.weekday()]
saturday = "Saturday"
sunday = "Sunday"
if(currentday == sunday):
    print("there is no school today")
    exit()
if(currentday == saturday):
    print("there is no school today")
    exit()

driver = webdriver.Firefox()


# Opens spork.school
driver.get("https://spork.school/")

# Logs into spork
id_usrname = driver.find_element_by_name("username")
id_usrname.send_keys(usernameid)
id_password = driver.find_element_by_name("password")
id_password.send_keys(passwordid)
login_button = driver.find_element_by_tag_name('button')
login_button.click()

## checks if login fails or not and goes to Schedule
time.sleep(3)
schedule_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/a[2]")

try:
    schedule_button.click()
    print("Login Success")
except:
   print("Login Failed or Connection timed out (if your connection timed out and you are sure you have WIFI, change the number of seconds in the sleep command to something higher)")
   exit()


time.sleep(2)
# gets the date and clicks on the schedule you have that day

monday = "Monday"
tuesday = "Tuesday"
wednesday = "Wednesday"
thursday = "Thursday"
friday = "Friday"

if(currentday == sunday):
    monday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[1]")
    monday_button.click()

if(currentday == tuesday):
    tuesday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[2]")
    tuesday_button.click()

if(currentday == wednesday):
    wednesday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[3]")
    wednesday_button.click()

if(currentday == thursday):
    thursday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[4]")
    thursday_button.click()

if(currentday == friday):
    friday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[5]")
    friday_button.click()
#asks if it is in the middle of the day
print("what is your next class (1 being your first class and 8 being your eighth class (if you have one))(This is not period)")
cj = int(input())
#Joins a class
print(str(cj))
#For 7 classes
print(str(zeroandeight))
if zeroandeight == ['No\n']:
    while cj <= 7:  
        try:
            join_button = driver.find_element_by_css_selector(".sign")
        except:
            time.sleep(1)
            pass
        else:
            playsound("joinclass.mp3")
            print("Type Y to join a class")
            check = input()
            if check == 'Y':
                join_button.click()
                print("you have joined a class")
                cj = cj + 1
                check = 'N'

if zeroandeight == ['Yes']:
    while cj <= 8:  
        try:
            join_button = driver.find_element_by_css_selector(".sign")
        except:
            time.sleep(1)
            pass
        else:
            print("Type Y to join a class")
            playsound("Thereclass.mp3")
            check = input()
            if check == 'Y':
                join_button.click()
                print("you have joined a class")
                cj = cj + 1
                check = 'N'

#quits the webbrowser
driver.quit()
            

        
            
