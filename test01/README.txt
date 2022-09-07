This is Django test program

you must go 
python manage.py migrate
python manage.py runserver

and you get these log...

=========
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 07, 2022 - 18:54:28
Django version 4.1.1, using settings 'test01.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[07/Sep/2022 18:54:38] "GET / HTTP/1.1" 200 2397
Not Found: /favicon.ico
[07/Sep/2022 18:54:39] "GET /favicon.ico HTTP/1.1" 404 2447
[07/Sep/2022 18:54:42] "GET /ajax/?input_data=aaa HTTP/1.1" 200 7
=========

so you should access to 
http://127.0.0.1:8000/
