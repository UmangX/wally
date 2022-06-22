from os import system
from os import listdir
from os import getlogin
from random import randint

username = getlogin()
main_dir = '/home/'+username+'/Pictures'
data_set = listdir(main_dir)
pic_set = data_set[randint(0,len(data_set))]
wally_command = 'feh --bg-fill '+main_dir+'/'+pic_set
system(wally_command)

