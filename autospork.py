
#!/usr/bin/env python
import os
import selenium
import time
import datetime
from datetime import date
import calendar
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from playsound import playsound
import PySimpleGUI as sg
home = os.path.expanduser("~")


sg.theme('DarkAmber')


### INPUT YOUR CREDENTIALS HERE ###


def FirstTimeSetup():
    
    
    layout = [
             [sg.Text('welcome to autosporklogin first time setup')],
             [sg.Text('Make sure firefox is installed')],
             [sg.Text('a donation to the paypal isaac.don7@gmail.com would be nice, but it is not necessary')],
             [sg.Text('I am not resposible for what you do with this tool')],
             [sg.Text('if you have less than 7 classes this will not work')],
             [sg.Text("by running, you agree to the liscence (MIT)")],
             [sg.Text('Please enter your spork credentials')], 
             [sg.Text('Username', size =(15, 1)), sg.InputText()], 
             [sg.Text('Password', size =(15, 1)), sg.InputText()],  
             [sg.Checkbox('Do you have a zero and eigth period', default=False, key="-IN-")], 
             [sg.Button('Confirm'), sg.Button('Cancel')] ]
    
    ###Setting Window
    window = sg.Window('Initial Setup', layout, size=(600,400))

    ###Showing the Application, also GUI functions can be placed here.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Cancel":
            exit()
            break
        elif values["-IN-"] == True:
            zeroeight = "Yes"
            break
        elif values["-IN-"] == False:
            zeroeight = "No"
            break
        elif event == 'Confirm':
            break

    window.close()
    userid = values[0]
    passid = values[1]
    f = open(home+"/autosporklogin/Login.txt", "a")
    f.write("%s"% userid+"\n")
    f.write("%s"% passid+"\n")
    f.write("%s"% zeroeight)
    f.close()
    
    return

def NotFirstTimeSetup():
    f = open(home+"/autosporklogin/Login.txt", "r")
    usernameid = f.readlines(1)
    passwordid = f.readlines(2)
    zeroandeight = f.readlines(3)
    return usernameid, passwordid, zeroandeight

def Login(usernameid, passwordid):
    id_usrname = driver.find_element_by_name("username")
    id_usrname.send_keys(usernameid)
    id_password = driver.find_element_by_name("password")
    id_password.send_keys(passwordid)
    login_button = driver.find_element_by_tag_name('button')
    login_button.click()
    return

def DateClick():
    my_date = date.today()
    currentday = calendar.day_name[my_date.weekday()]

    if(currentday == "Sunday"):
        print("there is no school today")
        exit()
    if(currentday == "Saturday"):
        print("there is no school today")
        exit()

    if(currentday == "Monday"):
        monday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[1]")
        monday_button.click()

    if(currentday == "Tuesday"):
        tuesday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[2]")
        tuesday_button.click()

    if(currentday == "Wednesday"):
        wednesday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[3]")
        wednesday_button.click()

    if(currentday == "Thursday"):
        thursday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[4]")
        thursday_button.click()

    if(currentday == "Friday"):
        friday_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/a[5]")
        friday_button.click()

    return

def schedclick():
    schedule_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/a[2]")

    try:
        schedule_button.click()
        print("Login Success")
    except:
        print("Login Failed or Connection timed out (if your connection timed out and you are sure you have WIFI, change the number of seconds in the sleep command to something higher)")
        exit()

    return
def joinbutton(jb):
    layout = [
             [sg.Text('A class is ready to join')], 
             [sg.Button('Join')],
             [sg.Button('Exit')] ]
    
    ###Setting Window
    window = sg.Window('A class is ready to join' , layout, size=(600,400))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            exit()
            break
        elif event == 'Join':
            jb.click()
            break

    window.close()

    return
def classjoiner(x, cj):
    layout = [
             [sg.Text('Attempting to join class number ' + str(cj))], 
             [sg.Button('Exit')] ]
    
    ###Setting Window
    window = sg.Window('Attempting to join class' , layout, size=(600,400))

    ###Showing the Application, also GUI functions can be placed here.

    while True:
        while cj <= x:  
            try:
                join_button = driver.find_element_by_css_selector(".sign")
            except:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event=="Exit":
                    exit()
                    break
                time.sleep(1)
                pass
            else:
                playsound("joinclass.mp3")
                joinbutton(join_button)
                cj = cj + 1
                   

    window.close()
 
    return

def Setting():
    layout = [
             [sg.Text('Settings')], 
             [sg.Checkbox('Headless (does not open up firefox)', default=False, key="-IN-")], 
             [sg.Button('Next'), sg.Button('Exit')] ]
    
    ###Setting Window
    window = sg.Window('Initial Setup', layout, size=(600,400))

    ###Showing the Application, also GUI functions can be placed here.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            exit()
            break
        elif values["-IN-"] == True:
            Headless = "Yes"
            break
        elif values["-IN-"] == False:
            Headless = "No"
            break
        elif event == 'Next':
            break

    window.close()
 
    
    return Headless
def midday():
    layout = [
             [sg.Text('Settings')], 
             [sg.Text('What class do you have (1 for first class)', size =(35, 1)), sg.InputText()],
             [sg.Button('Run'), sg.Button('Exit')] ]
    
    ###Setting Window
    window = sg.Window('midday', layout, size=(600,400))

    ###Showing the Application, also GUI functions can be placed here.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            exit()
            break
        elif event == 'Run':
            break

    window.close()
    classnum = values[0]

    
    return int(classnum)


##actual program
if(os.stat(home+"/autosporklogin/Login.txt").st_size == 0):
    FirstTimeSetup();
    
Head = Setting();


usernameid, passwordid, zeroandeight = NotFirstTimeSetup();

if Head == "Yes":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
else:
    driver = webdriver.Firefox()
    

# Opens spork.school
driver.get("https://spork.school/")

# Logs into spork
Login(usernameid, passwordid);

## checks if login fails or not and goes to Schedule
time.sleep(2)
schedclick();

time.sleep(2)
# gets the date and clicks on the schedule you have that day
DateClick();

#asks if it is in the middle of the day

cj = midday()


#For 7 classes

if zeroandeight == ['No']:
    cls = 7
else:
    cls = 8

classjoiner(cls , cj);

#quits the webbrowser
driver.quit()
exit()