import os
import time


"""
Webify Program

This script creates a folder directory for a new webiste to be stored on the desktop

This program also writes the initial connections between the javascript, html, and css files

"""

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

class Web_Folder:


    def __init__(self, new_folder):
        self.maindir = desktop + "\\Webify\\"
        self.dirpath = desktop + "\\Webify\\" + new_folder
        self.inside_directory = self.dirpath + "\\"

        if not os.path.exists(self.maindir):
            os.mkdir(self.maindir)

        if not os.path.exists(self.dirpath):
            os.mkdir(self.dirpath)

    def index(self):
        try:
            with open(os.path.dirname(os.path.realpath(__file__)) + "\\index.txt", 'r') as index_string:
                r = index_string.read()
            with open(self.inside_directory + "index.html", 'w') as html_file:
                html_file.write(r)
        except:
            print("Error Setting Up HTML Doc")
            time.sleep(4)

    def style(self):
        if not os.path.exists(self.inside_directory + "style"):
            os.makedirs(self.inside_directory + "style\\")
        with open(self.inside_directory + "style\\style.css", 'a'):
            os.utime(self.inside_directory + "style\\style.css", None)

    def js(self):
        if not os.path.exists(self.inside_directory + "js"):
            os.makedirs(self.inside_directory + "js\\")
        with open(self.inside_directory + "js\\main.js", 'a'):
            os.utime(self.inside_directory + "js\\main.js", None)

    def py(self):
        if not os.path.exists(self.inside_directory + "py"):
            os.makedirs(self.inside_directory + "py\\")
        with open(self.inside_directory + "py\\main.py", 'a'):
            os.utime(self.inside_directory + "py\\main.py", None)


folder_name = input("What is the name of your new Project?")
while len(folder_name) < 1 :
    if len(folder_name) == 0:
        print("Must Enter a valid web-folder name")
        folder_name = input("What is the name of your new Project?")

folder = Web_Folder(folder_name)

folder.index()
folder.style()
folder.js()
folder.py()


