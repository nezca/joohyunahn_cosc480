#!C:\Users\oldyt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html; charset=utf-8\n")
print()

"""This is the main page which provides core functions
   such as show the trekking course lists on the web and creates, updates and deletes.
"""
# This web service has been developed with a few frameworks of Python
# such as CGI, OS and html_sanitizer, also it has own module which is 'view.py'.
import cgi, os, view, html_sanitizer

# This code with sanitizer is to prevent
# that User will control the input box using Javascript language
sanitizer = html_sanitizer.Sanitizer()

# This code to store every info from the URL box of the Web
form = cgi.FieldStorage()

# If the ID of each web page exists on the URL box,
# this code will return 'pageid', 'description', 'update_link' and delete action,
# otherwise, just will return a statement for encourage to write a new course
if 'id' in form:
    title = pageid = form["id"].value
    description = open('data/'+pageid, 'r').read()
    description = sanitizer.sanitize(description)
    title = sanitizer.sanitize(title)
    update_link = '<b style="color:rgb(60,179,113); font-size:20px;"><a href="update.py?id={}">The written information on the above course is not correct, so I will revise it!!</a></b>'.format(pageid)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageid" value="{}">
            <input type="submit" value="This trekking course has to be deleted because it does not exist anymore!!" onclick="alert('Are you a valid person? or not?')">
        </form>
    '''.format(pageid)
else:
    pageid = "Let share your fantastic Trekking courses to everyone!"
    description = "Do you have the recommendable 'Trekking courses'?, just <strong>Click</strong> the below!"
    update_link = ''
    delete_action = ''

# From this line Python will start printing
# the 'HTML' codes for express on the web which is main page.
print('''<!doctype html>
<html>
<head>
  <title>TrekkPedia NZ</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body style="background-image: url('background.png'); font-family:verdana;">
  <div style="text-align:center;">
  <h1><a href="index.py">TrekkPedia NZ</a></h1>
  <picture>
    <sourse srcset="mains.png" media="(min-width:1024px)">
    <sourse srcset="mains.png" media="(min-width:768px)">
    <sourse srcset="mains.png" media="(min-width:320px)">
    <img src="mains.png" alt="New Zealand's trekking courses" alt="TrekkPedia" style="width:100%;">
  </picture>
  <br>
  <h2><b><strong style="color:DodgerBlue;">"TrekkPedia"</strong> is a free trekking course sharing service around New Zealand that anyone can participate in.
  Currently, Our TrekkPedia contains <strong style="color:DodgerBlue;">now</strong> <b style="color:red; font-size:50px;">{filecount}</b> courses csv files.</b></h2>
  <br>
  <h2>{title}</h2>
  <h3>{desc}</h3>
  <b style="color:rgb(60,179,113); font-size:30px;"><a href="create.py">I want to say my experience with wonderful trekking courses ever!!</a></b>
  <br>
  <br>
  {update_link}
  <br>
  <br>
  {delete_action}
  <br>
  <br>
  <p><b style="color:red;">(Tip)</b> You can use <strong style="color:DodgerBlue;">'Ctrl+F'</strong> for searching what you want to find certain trekking courses..</p>
  </div>
  <ul>
    {liststr}
  </ul>
</body>
<footer style="text-align:center;">
  <hr align="center" width="100%">
  <p>Written by Joo-Hyun Ahn | for COSC480 Project | MADS of UC 2019</p>
  <p>Contact information: <a href="mailto:oldyth@naver.com">oldyth@naver.com</a>, +64) 021 654 780</p>
</footer>
</html>
'''.format(title = pageid,
    desc = description,
    liststr = view.get_list(),
    update_link = update_link,
    delete_action = delete_action,
    filecount = view.count_list()))
