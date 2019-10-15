#!C:\Users\oldyt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html; charset=utf-8\n")
print()

"""This is the update page for updating the previous trekking course
   information which provides update function and users can check what users have updated.
"""
# This web service has been developed with a few frameworks of Python
# such as CGI, OS and hatml_sanitizer, also it has own module which is 'view.py'.
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
    pageid = form["id"].value
    description = open('data/'+pageid, 'r').read()
    description = sanitizer.sanitize(description)
else:
    pageid = "Welcome to TrekkPedia NZ"
    description = "Do you have the recommendable 'Trekourses'?"

# From this line Python will start printing
# the 'HTML' codes for express on the web which is update page.
print('''<!doctype html>
<html>
<head>
  <title>TrekkPedia NZ</title>
  <meta charset="utf-8">
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
  <h2>What's wrong of the information about {title} course?</h2>
  <h3>As you know, fresh information is welcome!!</h3>
  <form action="process_update.py" method="post">
      <input type="hidden" name="pageid" value="{form_default_title}">
      <p><b style="color:red;">(Tip)</b> When you try to revise the course name, please <strong style="color:DodgerBlue;">remove</strong> the <strong style="color:DodgerBlue;">'.csv'</strong> in the below box</p>
      <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
      <p><b style="color:red;">(Tip)</b>This web page is still being developed. I am sorry for your inconvenient.</p>
      <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
      <p><input type="submit" onclick="alert('The information has been better, are not you?')"></p>
  </form>
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
    form_default_title = pageid,
    form_default_description = description))
