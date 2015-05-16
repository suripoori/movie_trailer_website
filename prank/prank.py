__author__ = 'Suraj'

import os
import re

def rename_files():
    file_list = os.listdir(r"C:\Users\Suraj\Downloads\prank\prank")
    for file in file_list:
        try:
            file = "C:\\Users\\Suraj\\Downloads\\prank\\prank\\" + file
            new_file_name = re.sub('[0123456789]','',file)
            #print (new_file_name)
            os.rename(file,new_file_name)
        except FileNotFoundError:
            print("Could not find file %s" % file)
rename_files()
