import configparser
from os import getlogin
from os import path

username = getlogin();
config_location = '/home/'+username+'/.config/wally.ini'

if path.exists(config_location) == False:
    config = configparser.ConfigParser()
    print("select location")
    print("enter time in second or y for turing suffle off")
    time = input()
    config['setting'] = {'location' : '/home/'+username+'/Pictures' , 'timer' : time}
    with open(config_location, 'w') as config_file:
        config.write(config_file)
