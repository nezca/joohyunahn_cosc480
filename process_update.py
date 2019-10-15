#!C:\Users\oldyt\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os, view

"""This is the update process page for updating the previous trekking course information
   which provides get the information from the URL box
   such as trekking course name and description user has updated.
"""
form = cgi.FieldStorage()

# Given Title and Description values from 'Create box' of the main page
# will be revised in the 'Data' folder in this program like as '{revisedtitle}.csv'.
# Then immediately redirect to the given information page
pageid = form["pageid"].value
title = form["title"].value
description = form["description"].value

opend_file = open('data/'+pageid, 'w')
opend_file.write(description)
opend_file.close()

os.rename('data/'+pageid, 'data/'+title+".csv")

print("Location: index.py?id="+title+".csv")
print()
