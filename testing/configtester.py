import configparser
from os import getlogin
from os import path

username = getlogin();

if path.exists('/home/'+username+'/.config/wally.ini') == False:
    config = configparser.ConfigParser()
    print("select location")
    print("enter time in second or y for turing suffle off")
    time = input()
    config['setting'] = {'location' : '/home/'+username+'/Pictures' , 'timer' : time}
    with open('wally.ini', 'w') as config_file:
        config.write(config_file)
