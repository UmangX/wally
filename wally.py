#!/usr/bin/env python3

#importing the libraries in the files
from os import system
from os import listdir
from os import getlogin
from random import randint
from tkinter import filedialog
from tkinter import *

def if_dir_change():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()



#getting the username for the directories and path 
username = getlogin()

#assigning the name with username
#main_dir = '/home/'+username+'/Pictures'
main_dir = folder_selected

#using the list data structures for the storage and access of the file and images in the direstories 
data_set = listdir(main_dir)
pic_set = data_set[randint(0,len(data_set)-1)]

#using the system to execute a terminal command
wally_command = 'feh --bg-fill '+main_dir+'/'+pic_set
system(wally_command)

