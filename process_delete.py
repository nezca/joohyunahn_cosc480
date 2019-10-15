#!C:\Users\oldyt\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os, view

"""This is the delete process page for deleting the previous trekking course information
   which provides get the information from the URL box
   such as trekking course name and description user want to delete. 
"""
form = cgi.FieldStorage()

# Given Pageid value from 'Delete box' of the given information page
# will be removed in the 'Data' folder in this program.
# Then immediately redirect to the given information page
pageid = form["pageid"].value

os.remove('data/'+pageid)

print("Location: index.py")
print()
