# gunicorn config for ch8 project
wsgi_app = 'mysite.wsgi'
# bind = '0:8081'
bind = 'unix:/tmp/gunicorn.sock'
# chdir = '/home/shkim/pyBook/ch8'
# pythonpath = '/home/shkim/pyBook/ch8/venv/lib/python3.10/site-packages'
# user = 'shkim'
# group = 'shkim'
# workers = 3
daemon = True
accesslog = '/home/shkim/pyBook/ch8/logs/access.log'
errorlog = '/home/shkim/pyBook/ch8/logs/error.log'
