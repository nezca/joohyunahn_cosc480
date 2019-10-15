#!C:\Users\oldyt\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os, view

"""This is the creation process page for creating new trekking course information
   which provides get the information from the URL box
   such as trekking course name and description user has created. 
"""
form = cgi.FieldStorage()

# Given Title and Description values from 'Create box' of the main page
# will be stored in the 'Data' folder in this program like as '{title}.csv'.
# Then immediately redirect to the given information page
title = form["title"].value
description = form["description"].value

opend_file = open('data/'+title+".csv", 'w')
opend_file.write(description)
opend_file.close()

print("Location: index.py?id="+title+".csv")
print()
