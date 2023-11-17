#"Copyright Notice and Disclaimer. 
#© NORHEASTERN UNIVERSITY 2023 SW-24013 used with permission. All rights reserved."

import subprocess
import sys
from time import time, sleep
import random

 # Name of the default Android app activity 
START_ACTIVITY = 'de.rctrust.sms_ts/de.rctrust.sms_ts.SMSActivity'
STOP_ACTIVITY = 'de.rctrust.sms_ts'

# ADB Code examples of the different devices. Add yours instead.
ADB_ID = {
    'huawei-p8-lite-2017':'9DCDU17120000073',
    'samsung-galaxy-a53':'RZCT709T8EB',
    'nokia-53':'N0AA003687K42800100'
}

ADB_PATH = '/usr/bin/adb'

# Control events to initiate the Android app and tap the button to execute the SMS transmission.
class Phone(object):
    def __init__(self,path,adb_id):
        self.adb_path = path
        self.adb_id = adb_id

    def wake_up(self):
        sleep(1)
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input keyevent KEYCODE_WAKEUP'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(1)
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input keyevent 82'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

    def force_stop_messenger(self):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'am force-stop', STOP_ACTIVITY], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

    def return_to_homescreen(self):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input keyevent KEYCODE_HOME'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

    def start_messenger(self):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'am start -n', START_ACTIVITY], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(3)

    def tap(self,xy):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input tap {} {}'.format(xy[0],xy[1])], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

    def send_message(self,phone_num):
        sleep(1)
        self.tap(self.CONTACT_SELECT)             
        sleep(1)
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', "input text '{}'".format(phone_num)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)          
        sleep(3)
        self.tap(self.SEND_NAVIGATION)
        sleep(10)

    def leave_chat(self):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input keyevent 4'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

    def turn_off_screen(self):
        subprocess.Popen([self.adb_path, '-s', self.adb_id, 'shell', 'input keyevent 26'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Based on the graphical interface and phone screen, define the width & heigth dimensions:
# 1) to select the bar in order to write the receiver's phone number (CONTACT_SELECT)
# 2) to press the "send" button (SEND_NAVIGATION)
class Nokia_53(Phone):
    def __init__(self,path,adb_id):
        self.CONTACT_SELECT = (120,200)
        self.SEND_NAVIGATION = (120,350)
        super().__init__(path,adb_id)

class Samsung_Galaxy_A53(Phone):
    def __init__(self,path,adb_id):
        self.CONTACT_SELECT = (200,310)
        self.SEND_NAVIGATION = (200,580)
        super().__init__(path,adb_id)

class Huawei_P8_Lite_2017(Phone):
    def __init__(self,path,adb_id):
        self.CONTACT_SELECT = (220,420)
        self.SEND_NAVIGATION = (500,680)
        super().__init__(path,adb_id)

# Define your ADB device codes for the checks.
def init_device(dev):

    if dev == 'samsung-galaxy-a53':
        return Samsung_Galaxy_A53(ADB_PATH,'RZCT709T8EB')
    
    if dev == 'huawei-p8-lite-2017':
        return Huawei_P8_Lite_2017(ADB_PATH,'9DCDU17120000073')

    if dev == 'nokia-53':
        return Nokia_53(ADB_PATH,'N0AA003687K42800100')

    else:
        print('Error: unspecified device')
    
    sys.exit()


def main(device_string, phone_num, iterations):

    device = init_device(device_string)

    t_start = time()

    #rand_offset = 0
    rand_offset = random.uniform(0,90)
   
    sleep(rand_offset)

    # Based on the number of given iterations, send SMSs consecutively. 
    for i in range(iterations):
        print("Starting iteration ({}/{})".format(i+1,iterations))
        device.wake_up()
        device.force_stop_messenger()
        device.start_messenger()
        device.send_message(phone_num)
        print("SMS sent!")
        device.leave_chat()
        device.return_to_homescreen()
        device.turn_off_screen()
        rand_delay = random.uniform(0,2000)*0.001
        sleep(5+rand_delay)
    t_end = time()
    print("Process finished in {} seconds ({} seconds start offset)".format(t_end-t_start,rand_offset))

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1].lower(), sys.argv[2].lower(), int(sys.argv[3].lower()))
    else:  
        print('Error: unspecified argument')    
    sys.exit()

