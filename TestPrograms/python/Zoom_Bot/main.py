import subprocess
import pyautogui
import pyscreeze
import pymsgbox
import pytweening
import time
import pandas as pd
from datetime import datetime

DETACHED_PROCESS = 0x00000008 #Weird Stack Overflow big brain number

def openZoom():
    subprocess.Popen(r'C:\\Users\karth\AppData\Roaming\Zoom\bin\zoom.exe',
    shell=False, 
    stdin=None, 
    stdout=None, 
    stderr=None,
    close_fds=True,
    creationflags=DETACHED_PROCESS) #Long ass process to open zoom, other random stuff is to open without waiting application to return something
    time.sleep(5) #Giving time for Zoom to open
    
def clickJoin():
    joinBttn = pyscreeze.locateCenterOnScreen('join_button.png')
    print('Join a meeting button located')
    pyautogui.click(joinBttn)   #Clicking join button
    print('Join Meeting button clicked')
    time.sleep(5) #Giving time for page to change

def enterMeetingID(ID):
    pyautogui.write(ID) #typing in Meeting ID
    print('Meeting ID typed')
    pyautogui.press('enter') # clicking enter to submit
    print('Submitted Meeting ID')
    time.sleep(3) #Giving time for page to update

def enterPassword(psswd):
    pyautogui.write(psswd) #typing in password
    print('Entering Meeting Password')
    pyautogui.press('enter') #clicking enter key to submit
    print('Submitting Meeting Password')

def sign_in(meetingid, psswd, OAuth):
    if(OAuth == 'true'):
        openZoom() #Opening Zoom
        clickJoin() #Joining a meeting 
        enterMeetingID(meetingid) #Entering meeting ID
        time.sleep(8) #Extra time allotted for OAuth to complete 
        enterPassword(psswd) #The final touch
    else:
        openZoom() #Opening Zoom
        clickJoin() #Joining a meeting 
        enterMeetingID(meetingid) #Entering meeting ID 
        enterPassword(psswd) #The final touch

df = pd.read_csv('timings.csv') # Reading the file
'''
while True:
    
    now = datetime.now().strftime("%H:%M") # checking if time is in csv file
    if now in str(df['timings']):

        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        m_OAuth = str(row.iloc[0,3])
        
        sign_in(m_id, m_pswd, m_OAuth)
        time.sleep(40)
        print('Screw Zoom')
'''
sign_in('97200380554', 'SnZuT0d2dFhiTFh1RUt1VGtubStjZz09', 'true') #Testing purposes
                        